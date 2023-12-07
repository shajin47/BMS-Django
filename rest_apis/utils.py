from django.contrib.auth.models import Group, Permission
# from .models import CustomUser

def create_groups_and_permissions():
    # create admin group
    admin_group,created = Group.objects.get_or_create(name = 'Admin Group')


    # Assign permissions to the admin group (customize based on your needs)
    admin_permissions = [
        Permission.objects.get(codename = 'add_customuser'),
        Permission.objects.get(codename = 'change_customuser'),
        Permission.objects.get(codename = 'delete_customuser'),
    ]
    admin_group.permissions.set(admin_permissions)

    #create user Group
    user_group,created = Group.objects.get_or_create(name = 'User Group')
    user_permissions = [

    ]
    user_group.permissions.set(user_permissions)
