from rest_framework import serializers
from .models import Status, Type, Category, Subcategory, DDSRecord

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

class DDSRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DDSRecord
        fields = '__all__'

    def validate(self, data):
        if data['category'].type != data['type']:
            raise serializers.ValidationError("Категория не принадлежит выбранному типу.")

        if data['subcategory'].category != data['category']:
            raise serializers.ValidationError("Подкатегория не принадлежит выбранной категории.")

        return data
