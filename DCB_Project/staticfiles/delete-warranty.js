$(document).ready(function() {
    $('.delete-btn').click(function() {
        const row = $(this).closest('tr');
        const id = $(this).data('id');
        
        if (confirm('Are you sure you want to delete this warranty?')) {
            $.ajax({
                url: `dealer/warranty/delete/${id}/`,
                type: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'  // Django CSRF token
                },
                success: function(response) {
                    if (response.status === 'success') {
                        row.remove();
                        alert('Warranty deleted successfully.');
                    } else {
                        alert('Failed to delete warranty.');
                    }
                },
                error: function() {
                    alert('An error occurred.');
                }
            });
        }
    });
});

$(document).ready(function() {
    console.log("Delete script loaded");
    $('.delete-btn').click(function() {
        // existing code
    });
});
