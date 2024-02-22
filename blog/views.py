# blog/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from wagtail.models import Page
from .models import BlogPage
import json
import bleach


@csrf_exempt
@require_http_methods(["POST"])
def create_blog_page(request):
    try:
        data = json.loads(request.body)
        parent_page = Page.objects.get(id=4) # Replace <YOUR_BLOG_INDEX_PAGE_ID> with the actual ID
        # Convert the frozenset to a list and extend it with additional tags
        allowed_tags = list(bleach.sanitizer.ALLOWED_TAGS) + ['p', 'h2']

        cleaned_html = bleach.clean(data.get('body', ''), tags=allowed_tags, strip=True)
        blog_page = BlogPage(
            title=data.get('title', 'Default Title'),
            intro=data.get('intro', ''),
            body=cleaned_html,
            date=data.get('date', '2023-01-01'), # Use an appropriate default date or parse from input
            slug=data.get('slug', 'default-slug'),
        )
        parent_page.add_child(instance=blog_page)
        blog_page.save_revision()
        #blog_page_revision.submit_for_moderation()
        #blog_page.save_revision().publish() # Adjust to save as draft if needed

        # Ensure the page is unpublished (i.e., only a draft exists)
        blog_page.unpublish()

        return JsonResponse({"success": True, "message": "Blog page created successfully."})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})
