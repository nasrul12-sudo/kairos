import os

from ultralytics import YOLO
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import default_storage

MODEL_PATH = 'apps/nutrition/model/best.pt'
model_leaf = YOLO(MODEL_PATH)

def pageNutrition(request):
    return render(request, 'nutrition.html')

@csrf_exempt
def loadNutrition(request):
    if request.method == "POST" and request.FILES.get('image'):
        image_file = request.FILES["image"]

        img_path = default_storage.save(f"uploads/nutrition/{image_file.name}", image_file)
        full_img_path = os.path.join(settings.MEDIA_ROOT, img_path)

        results = model_leaf.predict(source=full_img_path, save=True, project=os.path.join(settings.MEDIA_ROOT, "outputs"), name="nutrition", exist_ok=True, conf=0.3)

        detected_path = os.path.join("outputs", "nutrition", os.path.basename(full_img_path))

        preds = []
        for r in results:
            for box in r.boxes:
                preds.append({
                    'label': model_leaf.names[int(box.cls)],
                    'confidence': float(box.conf),
                    'bbox': box.xyxy[0].tolist()
                })

        return JsonResponse({
            "status": "success",
            "original_image": settings.MEDIA_URL + img_path,
            "detected_image": settings.MEDIA_URL + detected_path,
            "predictions": preds
        })

    return JsonResponse({"error": "Invalid request"}, status=400)
