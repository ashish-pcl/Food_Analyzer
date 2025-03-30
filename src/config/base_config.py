import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "../../static/uploads")
    EDAMAM_APP_ID = "e3355226"
    EDAMAM_APP_KEY = "eb03795694782e311cfb1063255a8428"
    EDAMAM_API_URL = "https://api.edamam.com/api/nutrition-data"
    GCP_CREDENTIALS = {
        "type": "service_account",
        "project_id": "ai-agent-447611",
        "private_key_id": "b4ffc01497b7e92cda75a631f262997958dc78dd",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDAsZHKL65Mk+rF\n"
                        "pPZmM42ASzCnWgTLtTl9A2V5eqo47dxT3O+a/fvC+ONyr1F2Xj6ei6pfOeodrRKL\n"
                        "RMAGHVXFXq4m4nF4jb0HRu7CdEgC70heX3V5Wy4w4pYu3APcQMc67BjTuW8N7sAF\n"
                        "cJ0/LS3W0GhOHz44B09csnHvrnPVwUWKUJY4BRwNjguAgzS/cdlJw8QZG019tXyh\n"
                        "4E2hVcUGxPVXo2XQTBZcIQtND2SMjKD5Ianv1uk52bFOiBciyVpmLzHtnJTldK33\n"
                        "YKbUxCZW5xKnFoUXp41HysWr30ftLeaA9WVWfTsUleu0og4MWhtHP2tuZeZTQFA4\n"
                        "Nz+7rbRTAgMBAAECgf8PFOZTWKPZRA0dip9wEukMKNUxHW2MwqgqPnU3KuYiV5Ob\n"
                        "w/LMYhCth0UK1ka5Vy8QkXCN6CQd9Mv/OI9A28aX/SScGYdhHZMH1Xp+yF5iQKGw\n"
                        "xEZAR03hmfcCeUrfSvY47Ne2kPS17er4xXFQyqJvNj/0maNeiTUl0Pwpat/U2cci\n"
                        "s3j+FDjxrNL5QjeAI2IAQspfVQYe5Lwf2D9pUIONJB5KtTYY8pyEHKLja/+EaZw3\n"
                        "uLrJnHAxkP+zdjnXmhm0ywEekZRecOUAvZ4U1nkyYNmdWKaUwCEMyHkKx/fp34qz\n"
                        "aF+lxOl3cCD6PmfTLs8zf6V3i8oyV12RLBoI5MECgYEA4LrxmspRPm86h9ntMpIv\n"
                        "hy0LvGHQCawRhhmGZmP9o+OsQNRrizRSQXNMT1/G1G+9yk1mp5PjsQJkcxM5I+Oz\n"
                        "fJE5dJ5htoFK6XOO41YTEYRqjGbL1VpejFXKmlYDrjK1LRdW0sT1kDeVlIoygiXA\n"
                        "bh6o+12Jft8WDwbS/qLaW2ECgYEA24F1OHtbn+WYc1BhyZ1RfzX1d/K+wJ4mYIhP\n"
                        "3/tD1e87DkwqFwnD4hDNSTkvM81rB4uDUT414rNvZ4pPxvTOm9iE/ld1YejF6yUC\n"
                        "zvuYXcApmTXbQ65K411Cis7sOoJH6KAB+CpnEmXjycGKJW6rnDAgJ0GpBJMXMK1F\n"
                        "iVKdgDMCgYAGH9IZv826/9j+fsfiCu3UpzucpKXAvbm0h9mLzMnKv5egJKnRn1lm\n"
                        "gzffKeMHQwxPCRD1HCimWERYhnuWKMxpZqPEM9TB3oAmIIoSU/QtFAi7TsnbRJ0z\n"
                        "AduFnTZ4dtVNJ0escsWman1fEO0TcuftmFROlVv74yR8wFjbq6B7wQKBgQCpU20U\n"
                        "W/xrFRaL5bb5avTiF8K6e7PwLE9Yae6Lzm0ey8OXnONfEDZd3i4tzQH/iPeGQ3XS\n"
                        "JxY0QcyvZ39w74mtqNG2zcqL858xbESFXInF0CWGvYfd5sZ4K4nYQBT0cWl9Jmk+\ngZ8vDxAvo6+ofn29J1a2Ua1LDRh3gUJB00wSBwKBgQC1K1yXYh0NLdVYo2H2Nxwo\n"
                        "P3riOHSN58nn5jsOb7EMvV30RxpYl3LtsqQGZWnJ4vOs3auOrde2XDq2Fu0rrI7U\n"
                        "1UJ2OtpQX8UfQOWpOsxHt25+TBtVvVXzQieCzgm2FVoxuJkSJm5llaIF+ucet2eh\nEDyClbSDUQVGEXbq8h0U7A==\n-----END PRIVATE KEY-----\n",
        "client_email": "ai-agent@ai-agent-447611.iam.gserviceaccount.com",
        "client_id": "102302492237829970706",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ai-agent%40ai-agent-447611.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }
    