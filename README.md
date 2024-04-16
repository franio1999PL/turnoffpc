# TurnOffPC

Aplikacja `TurnOffPC` pozwala na zdalne wyłączanie komputera za pośrednictwem rekordu w bazie danych MySQL. Aplikacja sprawdza stan w tabeli `turnoffpc`, a gdy znajdzie rekord o wartości 'OFF', zmienia go na 'ON' i wyłącza komputer.

## Link do pobrania aplikacji [POBIERZ](https://storage.overhost.pl/TURNOFFPC.zip)

## Wymagania

Aplikacja została napisana w Pythonie i wymaga następujących zależności:

- Python 3.x
- PyMySQL
- PyInstaller (opcjonalnie, do tworzenia pliku .exe)

## Instalacja

Aby zainstalować niezbędne zależności, wykonaj poniższe kroki:

```bash
# Instalacja PyMySQL
pip install pymysql

# Instalacja PyInstaller
pip install pyinstaller
```

# Konfiguracja

```python
#Dane do bazy danych MYSQL/MARIADB
db_host = 'adres_hosta_bazy_danych'
db_user = 'nazwa_uzytkownika'
db_password = 'haslo'
db_name = 'nazwa_bazy_danych'
```
