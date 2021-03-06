# Generated by Django 4.0.3 on 2022-03-20 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_name', models.CharField(max_length=75)),
                ('Brand_logo', models.CharField(max_length=75)),
                ('Brand_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_first_name', models.CharField(max_length=50)),
                ('Order_middle_name', models.CharField(max_length=50)),
                ('Order_last_name', models.CharField(max_length=50)),
                ('Order_email', models.CharField(max_length=50)),
                ('Order_mobile', models.CharField(max_length=15)),
                ('Order_token', models.CharField(max_length=100)),
                ('Order_description', models.CharField(max_length=100)),
                ('Order_discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Order_item_discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Order_sub_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Order_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Order_grand_total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_first_name', models.CharField(max_length=50)),
                ('User_middle_name', models.CharField(max_length=50)),
                ('User_last_name', models.CharField(max_length=50)),
                ('User_email', models.CharField(max_length=50)),
                ('User_mobile', models.CharField(max_length=15)),
                ('User_password', models.CharField(max_length=32)),
                ('User_gender', models.CharField(max_length=15)),
                ('User_intro', models.TimeField()),
                ('User_profile', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Product_content',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_description',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_meta_title',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_purchase_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='Product_shop',
            field=models.CharField(default='null', max_length=40),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='User_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_account_user_name', models.CharField(max_length=50)),
                ('User_account_password', models.CharField(max_length=32)),
                ('User_account_hint_question', models.CharField(max_length=32)),
                ('User_account_answer', models.CharField(max_length=32)),
                ('User_account_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='User_product',
            field=models.ManyToManyField(to='e_commerce.product'),
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=100)),
                ('transaction_content', models.TextField()),
                ('transaction_type', models.SmallIntegerField()),
                ('transaction_mode', models.SmallIntegerField()),
                ('transaction_status', models.SmallIntegerField()),
                ('transaction_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.order')),
                ('transaction_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_type_name', models.CharField(max_length=75)),
                ('Product_type_description', models.CharField(max_length=100)),
                ('Product_type_product', models.ManyToManyField(to='e_commerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_review_name', models.CharField(max_length=75)),
                ('Product_review_ratin', models.SmallIntegerField()),
                ('Product_review_content', models.TextField()),
                ('Product_review_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_item_content', models.TextField()),
                ('Order_item_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Order_item_discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Product_quantity', models.IntegerField()),
                ('Order_item_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.order')),
                ('Order_item_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Order_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.user'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=75)),
                ('Category_meta_title', models.CharField(max_length=100)),
                ('Category_description', models.CharField(max_length=100)),
                ('Category_content', models.TextField()),
                ('Category_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.category')),
                ('Category_product', models.ManyToManyField(to='e_commerce.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Product_brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.brand'),
        ),
    ]
