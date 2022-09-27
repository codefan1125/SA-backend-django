# Generated by Django 2.1.13 on 2022-04-08 01:26

from django.db import migrations
from django.db import connection

def update_codes(apps, schema_editor):
    cursor_update = connection.cursor()
    sql_update = "UPDATE bp SET bp.BasingPointCode = LTRIM(STR(BasingPointID)) FROM [dbo].[BasingPoint] AS bp;"
    cursor_update.execute(sql_update)

    cursor_alter = connection.cursor()
    sql_alter = "ALTER TABLE [dbo].[BasingPoint] ADD UNIQUE (BasingPointCode);"
    cursor_alter.execute(sql_alter)

    cursor_update = connection.cursor()
    sql_update = "UPDATE bp SET bp.BasingPointCode = LTRIM(STR(BasingPointID)) FROM [dbo].[BasingPoint_History] AS bp;"
    cursor_update.execute(sql_update)

    cursor_alter = connection.cursor()
    sql_alter = "ALTER TABLE [dbo].[BasingPoint_History] ADD UNIQUE (BasingPointCode);"
    cursor_alter.execute(sql_alter)

    cursor_update = connection.cursor()
    sql_update = "UPDATE bp SET bp.CityCode = LTRIM(STR(CityID)) FROM [dbo].[City] AS bp;"
    cursor_update.execute(sql_update)

    cursor_alter = connection.cursor()
    sql_alter = "ALTER TABLE [dbo].[City] ADD UNIQUE (CityCode);"
    cursor_alter.execute(sql_alter)

    cursor_update = connection.cursor()
    sql_update = "UPDATE bp SET bp.CityCode = LTRIM(STR(CityID)) FROM [dbo].[City_History] AS bp;"
    cursor_update.execute(sql_update)

    cursor_alter = connection.cursor()
    sql_alter = "ALTER TABLE [dbo].[City_History] ADD UNIQUE (CityCode);"
    cursor_alter.execute(sql_alter)

class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0011_auto_20220407_2125'),
    ]

    operations = [
         #Invoke update_codes
         migrations.RunPython(update_codes, reverse_code=migrations.RunPython.noop),
    ]