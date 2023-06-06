# Generated by Django 2.2.6 on 2023-05-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bentuxianyou31',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True)),
                ('addqz', models.BigIntegerField(blank=True, null=True)),
                ('xyqz', models.BigIntegerField(blank=True, null=True)),
                ('fxqy', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bentuxianyou31',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Gnlssj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.BigIntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('province', models.TextField(blank=True, null=True)),
                ('confirm', models.BigIntegerField(blank=True, null=True)),
                ('dead', models.BigIntegerField(blank=True, null=True)),
                ('heal', models.BigIntegerField(blank=True, null=True)),
                ('confirm_add', models.TextField(blank=True, null=True)),
                ('confirm_cuts', models.TextField(blank=True, null=True)),
                ('dead_cuts', models.TextField(blank=True, null=True)),
                ('now_confirm_cuts', models.TextField(blank=True, null=True)),
                ('heal_cuts', models.TextField(blank=True, null=True)),
                ('newconfirm', models.BigIntegerField(blank=True, db_column='newConfirm', null=True)),
                ('newheal', models.BigIntegerField(blank=True, db_column='newHeal', null=True)),
                ('newdead', models.BigIntegerField(blank=True, db_column='newDead', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('wzz', models.BigIntegerField(blank=True, null=True)),
                ('wzz_add', models.BigIntegerField(blank=True, null=True)),
                ('dateid', models.TextField(blank=True, db_column='dateId', null=True)),
            ],
            options={
                'db_table': 'gnlssj',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='J2Ylj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm', models.BigIntegerField(blank=True, null=True)),
                ('nowconfirm', models.BigIntegerField(blank=True, db_column='nowConfirm', null=True)),
                ('nowsevere', models.BigIntegerField(blank=True, db_column='nowSevere', null=True)),
                ('noinfecth5', models.BigIntegerField(blank=True, db_column='noInfectH5', null=True)),
                ('local_acc_confirm', models.BigIntegerField(blank=True, null=True)),
                ('dead', models.BigIntegerField(blank=True, null=True)),
                ('healrate', models.TextField(blank=True, db_column='healRate', null=True)),
                ('deadrate', models.TextField(blank=True, db_column='deadRate', null=True)),
                ('localconfirm', models.BigIntegerField(blank=True, db_column='localConfirm', null=True)),
                ('suspect', models.BigIntegerField(blank=True, null=True)),
                ('heal', models.BigIntegerField(blank=True, null=True)),
                ('importedcase', models.BigIntegerField(blank=True, db_column='importedCase', null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('y', models.TextField(blank=True, null=True)),
                ('noinfect', models.BigIntegerField(blank=True, db_column='noInfect', null=True)),
                ('localconfirmh5', models.BigIntegerField(blank=True, db_column='localConfirmH5', null=True)),
                ('dateid', models.TextField(blank=True, db_column='dateId', null=True)),
            ],
            options={
                'db_table': 'j2ylj',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='J2Yxz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dead', models.BigIntegerField(blank=True, null=True)),
                ('heal', models.BigIntegerField(blank=True, null=True)),
                ('importedcase', models.BigIntegerField(blank=True, db_column='importedCase', null=True)),
                ('infect', models.BigIntegerField(blank=True, null=True)),
                ('localinfectionadd', models.BigIntegerField(blank=True, null=True)),
                ('localconfirmadd', models.BigIntegerField(blank=True, db_column='localConfirmadd', null=True)),
                ('suspect', models.BigIntegerField(blank=True, null=True)),
                ('deadrate', models.TextField(blank=True, db_column='deadRate', null=True)),
                ('healrate', models.TextField(blank=True, db_column='healRate', null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('y', models.TextField(blank=True, null=True)),
                ('confirm', models.BigIntegerField(blank=True, null=True)),
                ('dateid', models.TextField(blank=True, db_column='dateId', null=True)),
            ],
            options={
                'db_table': 'j2yxz',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mrsj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmedcount', models.BigIntegerField(blank=True, db_column='confirmedCount', null=True)),
                ('confirmedincr', models.BigIntegerField(blank=True, db_column='confirmedIncr', null=True)),
                ('curedcount', models.BigIntegerField(blank=True, db_column='curedCount', null=True)),
                ('curedincr', models.BigIntegerField(blank=True, db_column='curedIncr', null=True)),
                ('currentconfirmedcount', models.BigIntegerField(blank=True, db_column='currentConfirmedCount', null=True)),
                ('currentconfirmedincr', models.BigIntegerField(blank=True, db_column='currentConfirmedIncr', null=True)),
                ('dateid', models.BigIntegerField(blank=True, db_column='dateId', null=True)),
                ('deadcount', models.BigIntegerField(blank=True, db_column='deadCount', null=True)),
                ('deadincr', models.BigIntegerField(blank=True, db_column='deadIncr', null=True)),
                ('highdangercount', models.BigIntegerField(blank=True, db_column='highDangerCount', null=True)),
                ('middangercount', models.BigIntegerField(blank=True, db_column='midDangerCount', null=True)),
                ('suspectedcount', models.BigIntegerField(blank=True, db_column='suspectedCount', null=True)),
                ('suspectedcountincr', models.BigIntegerField(blank=True, db_column='suspectedCountIncr', null=True)),
            ],
            options={
                'db_table': 'mrsj',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ssrd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventdescription', models.TextField(blank=True, db_column='eventDescription', null=True)),
                ('eventtime', models.TextField(blank=True, db_column='eventTime', null=True)),
                ('eventurl', models.TextField(blank=True, db_column='eventUrl', null=True)),
                ('homepageurl', models.TextField(blank=True, db_column='homepageUrl', null=True)),
                ('item_avatar', models.TextField(blank=True, null=True)),
                ('sitename', models.TextField(blank=True, db_column='siteName', null=True)),
            ],
            options={
                'db_table': 'ssrd',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Xyyq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincename', models.TextField(blank=True, db_column='provinceName', null=True)),
                ('cityname', models.TextField(blank=True, db_column='cityName', null=True)),
                ('currentconfirmedcount', models.TextField(blank=True, db_column='currentConfirmedCount', null=True)),
                ('confirmedcount', models.TextField(blank=True, db_column='confirmedCount', null=True)),
                ('curedcount', models.TextField(blank=True, db_column='curedCount', null=True)),
                ('deadcount', models.TextField(blank=True, db_column='deadCount', null=True)),
            ],
            options={
                'db_table': 'xyyq',
                'managed': True,
            },
        ),
    ]
