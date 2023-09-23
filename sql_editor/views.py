from django.shortcuts import render, redirect
from .models import Query
from .forms import QueryForm
from django.db import connection
from django.contrib import messages

def help_page(request):
    return render(request, 'help_page.html')

def sql_tables_view(request):
    return render(request, 'sql_tables.html')

def about(request):
    return render(request, 'about.html')

from django.contrib import messages  # Import the messages framework

# ...

def sql_editor(request):
    success_message = None  # Initialize success_message to None

    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            sql_text = form.cleaned_data['sql_text']
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql_text)
                    result = cursor.fetchall()
                result = "\n".join([str(row) for row in result])

                # Set success_message when query is executed successfully
                success_message = 'Query executed successfully!'

            except Exception as e:
                result = str(e)
                # Add an error message
                messages.error(request, f'Error executing query: {str(e)}')

            Query.objects.create(sql_text=sql_text, result=result)

    else:
        form = QueryForm()
        result = None

    # Pass success_message to the template
    return render(request, 'sql_editor/editor.html', {'form': form, 'result': result, 'success_message': success_message})
