from rest_framework import permissions


class Owner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        :param request: request
        :param view: view
        :param obj: obj
        :return: boolean
        """
        return obj.user == request.user
