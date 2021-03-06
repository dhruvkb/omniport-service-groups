from formula_one.serializers.generics.contact_information import (
    ContactInformationSerializer,
)
from groups.serializers.group_mixin import GroupSerializerMixin


class GroupContactInformationSerializer(
    GroupSerializerMixin,
    ContactInformationSerializer
):
    """
    Extend the ContactInformationSerializer for a particular group
    """

    def update(self, instance, validated_data):
        """
        Drop the slug from the submitted data and defer to the base
        implementation of the function
        :param instance: the instance being updated
        :param validated_data: the new validated data
        :return: the updated instance
        """

        if 'slug' in validated_data:
            del validated_data['slug']

        return super().update(instance, validated_data)

    def create(self, validated_data):
        """
        Create a blank contact information instance and convert the save
        operation into an update operation
        :param validated_data: the new validated data
        :return: the newly created instance
        """

        group = validated_data.pop('slug')
        instance, created = group.contact_information.get_or_create()

        return super().update(instance, validated_data)
