@REM Development
SET DB_NAME=appointment
SET DB_USER=postgres
SET DB_USER_PASSWORD=postgres
SET DB_HOST=localhost
SET DB_PORT=5432
SET DATABASE_URL=postgresql://DB_USER:DB_USER_PASSWORD@localhost:5432/DB_NAME?sslmode=disable

@REM Production
@REM SET DB_NAME=appointmentdb
@REM SET DB_USER=appointmentdb_eoli_user
@REM SET DB_USER_PASSWORD=SMQR1tNhKYj4AaxBJTXz7S7d7r3OVzju
@REM SET DB_HOST=dpg-ct4dg33tq21c73934kug-a
@REM SET DB_PORT=5432
@REM SET DATABASE_URL=postgresql://appointmentdb_eoli_user:SMQR1tNhKYj4AaxBJTXz7S7d7r3OVzju@dpg-ct4dg33tq21c73934kug-a/appointmentdb_eoli

SET EMAIL_HOST=smtp.gmail.com
SET EMAIL_HOST_USER=ericknabstar@gmail.com
SET DEFAULT_FROM_EMAIL=ericknabstar@gmail.com
SET EMAIL_HOST_PASSWORD=azcwouvktbqpbfro
SET EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend



