import pymysql
import os
import time

db_host = 'adres_hosta_bazy_danych'
db_user = 'nazwa_uzytkownika'
db_password = 'haslo'
db_name = 'nazwa_bazy_danych'

first_run = True  # Zmienna do śledzenia pierwszego uruchomienia

def setup_database():
    connection = pymysql.connect(host=db_host,
                                 user=db_user,
                                 password=db_password,
                                 database=db_name,
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Sprawdzenie, czy tabela 'turnoffpc' istnieje
            cursor.execute("SHOW TABLES LIKE 'turnoffpc'")
            result = cursor.fetchone()
            if not result:
                # Tworzenie tabeli, jeśli nie istnieje
                sql = """
                CREATE TABLE turnoffpc (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    pc_name VARCHAR(255) NOT NULL,
                    command VARCHAR(10) NOT NULL
                )
                """
                cursor.execute(sql)
                print("Tabela 'turnoffpc' została utworzona.")
            else:
                print("Tabela 'turnoffpc' już istnieje.")

def check_and_update_command():
    global first_run  # Używamy zmiennej globalnej
    connection = pymysql.connect(host=db_host,
                                 user=db_user,
                                 password=db_password,
                                 database=db_name,
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Sprawdzanie, czy rekord już istnieje
            sql = "SELECT command FROM turnoffpc WHERE pc_name = 'kiemek'"
            cursor.execute(sql)
            result = cursor.fetchone()

            if result:
                if result['command'] == 'OFF':
                    if first_run:
                        # Tylko zmiana na ON, bez wyłączania komputera
                        sql = "UPDATE turnoffpc SET command = 'ON' WHERE pc_name = 'kiemek'"
                        cursor.execute(sql)
                        connection.commit()
                        print("Stan komputera zmieniony na ON.")
                    else:
                        # Wyłącz komputer przy kolejnych uruchomieniach
                        sql = "UPDATE turnoffpc SET command = 'ON' WHERE pc_name = 'kiemek'"
                        cursor.execute(sql)
                        connection.commit()
                        print("Komputer zostanie wyłączony.")
                        os.system('shutdown /s /t 1')
                else:
                    print("Komputer pozostaje włączony.")
            else:
                # Tworzenie rekordu, jeśli nie istnieje
                sql = "INSERT INTO turnoffpc (pc_name, command) VALUES ('kiemek', 'ON')"
                cursor.execute(sql)
                connection.commit()
                print("Utworzono nowy rekord dla 'kiemek' z komendą 'ON'.")

            # Aktualizacja zmiennej first_run
            first_run = False

def main_loop():
    setup_database()
    while True:
        check_and_update_command()
        time.sleep(60)  # Sprawdzanie stanu co minutę

if __name__ == '__main__':
    main_loop()
