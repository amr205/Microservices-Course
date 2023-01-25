from django.core.management.base import BaseCommand, CommandError
import pika, time, json
from django.conf import settings
from recommendations_app.models import User, Genre

def handle_profile_service_messages(ch, method, properties, body):
    json_data = json.loads(body)
    user, _ = User.objects.get_or_create(
        id=json_data['profile']['_id'],
    )
    user.genres.all().delete()

    genres = json_data['profile']['favorite_genres']
    for genre_name in genres:
        genre, _ = Genre.objects.get_or_create(
            name=genre_name,
        )
        user.genres.add(genre)
    return


class Command(BaseCommand):
    help = 'Listen to messages in the profileservice queue'

    def handle(self, *args, **options):
        time.sleep(8)
        print("Connecting to service bus")
        url = settings.AMQP_URL
        params = pika.URLParameters(url)
        params.socket_timeout = 5

        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='profileservice', durable=True)

        channel.basic_consume('profileservice', handle_profile_service_messages, auto_ack=True)
        channel.start_consuming()

        connection.close()


