# finance
fin_app

В случае если докер не запустится, проект можно запустить локально  **python manage.py runserver**


Проект содержит два пути:
/admin

/fin_app/

   fin_app/home/ [name='home']

   fin_app/api/
   
   fin_app/new/ [name='create_organization']
   
   fin_app/edit/<int:pk>/ [name='edit_organization']
   
   fin_app/login/ [name='login']
   
   fin_app/logout/ [name='logout']
   
   fin_app/register/ [name='register']

Есть распределение по ролям Куратор и Ревьюер. Настройки для каждой из ролей и групп можно просмотреть в админ панели root:admin123.
