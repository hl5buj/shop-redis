from django import template

# 템플릿 태그 라이브러리 등록
register = template.Library()

@register.filter
def multiply(value, arg):
    """
    두 숫자를 곱하는 템플릿 필터

    사용 예: {{ price|multiply:quantity }}
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def currency(value):
    """
    숫자를 천 단위 쉼표가 있는 통화 형식으로 변환하는 필터

    사용 예: {{ price|currency }}
    출력 예: 1,234,567
    """
    try:
        # 숫자를 정수로 변환 후 천 단위 쉼표 추가
        return "{:,}".format(int(float(value)))
    except (ValueError, TypeError):
        return value
