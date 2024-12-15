# Django TemplateView and RedirectView

A Django project demonstrating the use of `TemplateView` and `RedirectView` to create dynamic and user-friendly web applications. This repository is ideal for developers looking to learn or enhance their skills in using Django's generic class-based views.

## Features

- **TemplateView** for rendering templates with context data.
- **RedirectView** for redirecting users to specific URLs.
- Customization options for dynamic URL routing and context data.
- Example implementations for common use cases.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shahramsamar/Django_templateview_reditectview.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Django_templateview_reditectview
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the application at `http://127.0.0.1:8000/`.

2. Examples of usage:
   - A `TemplateView` renders a static or dynamic template.
   - A `RedirectView` redirects the user to another URL based on logic or predefined routes.

## Example Code

### TemplateView Example
```python
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Welcome to the Home Page!"
        return context
```

### RedirectView Example
```python
from django.views.generic.base import RedirectView

class RedirectToGoogleView(RedirectView):
    url = "https://www.google.com"
```

### URL Configuration
```python
from django.urls import path
from .views import HomePageView, RedirectToGoogleView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('google/', RedirectToGoogleView.as_view(), name='redirect_to_google'),
]
```

## Requirements

- Python 3.7+
- Django 3.2+

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

- **Author**: Shahramsamar
- **Email**: [shahramsamar2010@gmail.com](mailto:shahramsamar2010@gmail.com)
- **GitHub**: [Shahramsamar](https://github.com/shahramsamar)

![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")
