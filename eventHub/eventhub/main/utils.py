from django.db.models import Q

class FilterManager:
    @staticmethod
    def apply_filters(queryset, request, allowed_fields):

        filters = Q()
        sorting = request.GET.get("sort_by")

        for field in allowed_fields:
            value = request.GET.get(field)
            if value:
                filters &= Q(**{f"{field}__icontains": value})

        queryset = queryset.filter(filters)

        if sorting in allowed_fields or (sorting and sorting.startswith("-") and sorting[1:] in allowed_fields):
            queryset = queryset.order_by(sorting)

        return queryset
