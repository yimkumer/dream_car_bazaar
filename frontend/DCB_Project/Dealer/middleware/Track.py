from ProductManagement.models import Lead


class TrackExploredPagesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        group_list = request.user.groups.values_list('name', flat=True)
        if request.user.is_authenticated:
            # Check if the page was already visited in this session
            visited_pages = request.session.get('visited_pages', [])
            current_page = request.path

            if current_page not in visited_pages:
                visited_pages.append(current_page)
                request.session['visited_pages'] = visited_pages

                # Update the Lead model
                lead, created = Lead.objects.get_or_create(user=request.user)
                lead.explored_pages += 1
                lead.save()

        return response
