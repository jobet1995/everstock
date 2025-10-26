from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.utils.html import strip_tags

from wagtail.models import Page

# To enable logging of search queries for use with the "Promoted search results" module
# <https://docs.wagtail.org/en/stable/reference/contrib/searchpromotions.html>
# uncomment the following line and the lines indicated in the search function
# (after adding wagtail.contrib.search_promotions to INSTALLED_APPS):

# from wagtail.contrib.search_promotions.models import Query


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)

        # To log this query for use with the "Promoted search results" module:

        # query = Query.get(search_query)
        # query.add_hit()

    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )


def ajax_search(request):
    """
    AJAX search endpoint that returns JSON results
    """
    search_query = request.GET.get("query", None)
    
    if not search_query or len(search_query.strip()) < 2:
        return JsonResponse({
            'results': []
        })
    
    # Search
    search_results = Page.objects.live().search(search_query)
    
    # Format results for JSON response
    results = []
    for result in search_results[:5]:  # Limit to 5 results
        # Get search description or excerpt from content
        excerpt = getattr(result, 'search_description', '')
        if not excerpt and hasattr(result, 'body'):
            # Try to get excerpt from body content if it exists
            try:
                excerpt = str(result.body)[:150] + '...' if len(str(result.body)) > 150 else str(result.body)
                excerpt = strip_tags(excerpt)
            except:
                excerpt = ''
        
        results.append({
            'title': str(result),
            'url': result.url,
            'excerpt': excerpt or 'No description available'
        })
    
    return JsonResponse({
        'results': results
    })