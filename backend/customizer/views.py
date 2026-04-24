from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Design
from .utils import apply_design


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    data = [{"id": p.id, "name": p.name} for p in products]
    return Response(data)


@api_view(['POST'])
def render_image(request):
    try:
        # 📥 Get data
        design = request.FILES.get('design')
        product_id = request.data.get('product')

        print("PRODUCT ID:", product_id)
        print("DESIGN FILE:", design)

        if not design or not product_id:
            return Response({"error": "Missing data"}, status=400)

        # 📦 Get product
        product = Product.objects.get(id=product_id)

        # 💾 Save design
        d = Design.objects.create(image=design)

        # 🎨 Apply design
        output = apply_design(
            product.base_image.path,
            d.image.path,
            product.x,
            product.y,
            product.width,
            product.height
        )

        # 🔥 DEBUG (VERY IMPORTANT)
        print("OUTPUT FILE:", output)
        print("FINAL URL SENT:", f"/media/{output}")

        # ✅ FINAL RESPONSE (THIS FIXES YOUR ISSUE)
        return Response({
            "image": f"/media/{output}"
        })

    except Exception as e:
        print("ERROR:", str(e))
        return Response({"error": str(e)}, status=500)