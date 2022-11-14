def work_with_db():
    print("Połączono do bazy danych")
    raise ConnectionAbortedError


def close_connection_db():
    print("Zamknięto DB")


try:
    work_with_db()
except ConnectionResetError:
    print("Zresetowało nam połączenie")
finally:
    close_connection_db()

