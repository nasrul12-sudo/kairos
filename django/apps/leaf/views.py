import os
import supabase

from ultralytics import YOLO
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import default_storage
from .utils.disease_data import DISEASE_ANALYSIS

MODEL_PATH = 'apps/leaf/model/best.pt'
model_leaf = YOLO(MODEL_PATH)

def pageLeaf(request):
    return render(request, 'upload_leaf.html')

@csrf_exempt
def loadLeaf(request):
    if request.method == "POST" and request.FILES.get('image'):
        image_file = request.FILES["image"]

        img_path = default_storage.save(f"uploads/leaf/{image_file.name}", image_file)
        full_img_path = os.path.join(settings.MEDIA_ROOT, img_path)

        results = model_leaf.predict(source=full_img_path, save=True, project=os.path.join(settings.MEDIA_ROOT, "outputs"), name="leaf", exist_ok=True, conf=0.3)

        detected_path = os.path.join("outputs", "leaf", os.path.basename(full_img_path))

        preds = []
        analysis = []
        for r in results:
            for box in r.boxes:
                class_name = model_leaf.names[int(box.cls)]
                confidence = float(box.conf)

                preds.append({
                    'label': class_name,
                    'confidence': confidence,
                    'bbox': box.xyxy[0].tolist()
                })

                if class_name in DISEASE_ANALYSIS:
                    desease_info = DISEASE_ANALYSIS[class_name]
                    desease_info['confidence'] = round(confidence, 2)
                    analysis.append(desease_info)

        # supabase.table*('leaf_detections').insert({
        #     "user_id": user_id,
        # })
        # print(analysis)
        return JsonResponse({
            "status": "success",
            "original_image": settings.MEDIA_URL + img_path,
            "detected_image": settings.MEDIA_URL + detected_path,
            "predictions": preds,
            "analysis": analysis
        })

    return JsonResponse({"error": "Invalid request"}, status=400)
