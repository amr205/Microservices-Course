IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'django_db')
BEGIN
    CREATE DATABASE [django_db]
END