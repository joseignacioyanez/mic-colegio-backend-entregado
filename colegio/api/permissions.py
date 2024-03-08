from rest_framework import permissions

class GroupsPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        permissions_allowed = {
            'administradores': {
                    'alumno': ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'],
                    'examenteorico': ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'],
                    'practica': ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'],
                    'examenteoricoalumno': ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'],
                    'practicaalumno': ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'],
                    'profesoresdiseniopractica': ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'],
                    'profesor': ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'],
            },
            'gestores': {
                    'alumno': ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'],
                    'profesor': ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy'],
            },
            'consultores': {
                    'alumno': ['list', 'retrieve'],
                    'profesor': ['list', 'retrieve'],
            }
        }
        # Extrarct what is requested
        user_groups = request.user.groups.values_list('name', flat=True)
        required_actions = [view.action]
        model_name = view.queryset.model.__name__.lower()


        # Compare what is requested with what is allowed
        for group_name in user_groups:
            if group_name in permissions_allowed:
                allowed_models = permissions_allowed[group_name]
                if model_name in allowed_models:
                    model_permissions = allowed_models[model_name]
                    for action in required_actions:
                        if action in model_permissions:
                            return True

        return False