# finance
fin_app

В случае если докер не запустится, проект можно запустить локально  **python manage.py runserver**


Проект содержит два пути:
/admin

/fin_app/

   home/ [name='home']

   api/
   
   new/ [name='create_organization']
   
   edit/<int:pk>/ [name='edit_organization']
   
   login/ [name='login']
   
   logout/ [name='logout']
   
   register/ [name='register']

Есть распределение по ролям Куратор и Ревьюер. Настройки для каждой из ролей и групп можно просмотреть в админ панели root:admin123.
