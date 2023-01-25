from django.core.management.base import BaseCommand, CommandError
import pika, time, json
from django.conf import settings
from recommendations_app.models import Song, Genre

def handle_songs_service_messages(ch, method, properties, body):
    json_data = json.loads(body)
    song, _ = Song.objects.get_or_create(
        name=json_data['song']['name'],
        defaults={'number_of_likes': 0},
    )

    if json_data['action'] == 'liked':
        song.number_of_likes = song.number_of_likes+1
    else:
        song.number_of_likes = song.number_of_likes-1
    
    song.genres.all().delete()

    genres = json_data['song']['genres']
    for genre_data in genres:
        genre, _ = Genre.objects.get_or_create(
            name=genre_data['name'],
        )
        song.genres.add(genre)
    song.save()
    return


class Command(BaseCommand):
    help = 'Listen to messages in the songservice queue'

    def handle(self, *args, **options):
        time.sleep(8)
        print("Connecting to service bus")
        url = settings.AMQP_URL
        params = pika.URLParameters(url)
        params.socket_timeout = 5

        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='songservice', durable=True)

        channel.basic_consume('songservice', handle_songs_service_messages, auto_ack=True)
        channel.start_consuming()

        connection.close()


