from rest_framework.response import Response
from rest_framework.views import APIView


class Candlestick(APIView):
    def get(self, request):
        data = [
            { 
                "x": "2024-09-04", 
                "open": 159.3, 
                "high": 163.88, 
                "low": 158.95, 
                "close": 160.87
            },
            { 
                "x": "2024-09-05", 
                "open": 161.54, 
                "high": 164.59, 
                "low": 161.05, 
                "close": 163.7
            },
            { 
                "x": "2024-09-06", 
                "open": 164.89, 
                "high": 165.41, 
                "low": 156.01, 
                "close": 156.82
            },
            { 
                "x": "2024-09-09", 
                "open": 160.76, 
                "high": 163.1, 
                "low": 160.25, 
                "close": 162.78
            },
            { 
                "x": "2024-09-10", 
                "open": 162.89, 
                "high": 162.89, 
                "low": 157.69, 
                "close": 162.43
            },
        ]

        return Response(data)


class Line(APIView):
    def get(self, request):
        data = {
                "labels": ["Jan", "Feb", "Mar", "Apr"],
                "data": [10, 20, 30, 40]
        }

        return Response(data)


class Bar(APIView):
    def get(self, request):
        data = {
            "labels": ["Product A", "Product B", "Product C"],
            "data": [100, 150, 200]
        }

        return Response(data)


class Pie(APIView):
    def get(self, request):
        data = {
            "labels": ["Red", "Blue", "Yellow"],
            "data": [300, 50, 100]
        }

        return Response(data)
