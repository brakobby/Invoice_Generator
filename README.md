# 📄 Invoice Generator

A modern, web-based invoice generation system built with **Django** and **Django Templates**. Perfect for freelancers, small businesses, and anyone who needs to create professional invoices quickly.

## 🚀 Features

- **User Authentication** - Secure registration and login system
- **Customer Management** - Add and manage client information
- **Invoice Creation** - Create professional invoices with line items
- **PDF Export** - Generate and download branded PDF invoices
- **Status Tracking** - Track invoice status (Draft, Sent, Paid, Overdue)
- **Dashboard** - Beautiful overview of your invoicing activity
- **Responsive Design** - Works perfectly on desktop and mobile

## 🛠 Tech Stack

### Backend
- **Django** - Python web framework
- **PostgreSQL** - Production database
- **SQLite** - Development database
- **Django Authentication** - Secure user management
- **WeasyPrint** - PDF generation

### Frontend
- **Django Templates** - Server-side rendering
- **Tailwind CSS** - Modern styling
- **JavaScript** - Interactive features
- **HTML5** - Semantic markup

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/invoice-generator.git
cd invoice-generator
```

### 2. Backend Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements/development.txt

# Run migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

### 3. Access the Application
- **Main Application**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## 🎯 Quick Start

1. **Register** a new account or **Login** with existing credentials
2. **Setup Your Company** - Add your company details and logo
3. **Add Customers** - Populate your client database
4. **Create Invoices** - Generate professional invoices in minutes
5. **Download PDFs** - Send branded invoices to your clients

## 📱 Main Pages

- **Dashboard** - `/` - Overview of your business
- **Invoices** - `/invoices/` - Manage all invoices
- **Customers** - `/customers/` - Client management
- **Create Invoice** - `/invoices/create/` - New invoice form
- **Profile** - `/profile/` - Company settings

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the backend directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=invoice_generator
DB_USER=your-username
DB_PASSWORD=your-password
```

### Database Setup
The project uses:
- **SQLite** for development (default)
- **PostgreSQL** for production

## 🗂 Project Structure

```
invoice-generator/
├── backend/                 # Django project
│   ├── apps/
│   │   ├── users/          # User authentication & profiles
│   │   ├── invoices/       # Invoice management
│   │   ├── customers/      # Customer CRM
│   │   └── core/           # Common utilities
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Base template
│   │   ├── dashboard.html  # Main dashboard
│   │   └── invoices/       # Invoice templates
│   ├── static/             # CSS, JS, images
│   ├── media/              # User uploads (logos, PDFs)
│   └── config/             # Django settings
├── requirements/           # Python dependencies
└── README.md
```

## 🎨 Customization

### Branding
- Upload your company logo
- Customize colors in profile settings
- Modify invoice templates

### Styling
- Built with Tailwind CSS
- Fully responsive design
- Easy to customize colors and layout

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

**Port already in use:**
```bash
python manage.py runserver 8001
```

**Migration issues:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Static files not loading:**
```bash
python manage.py collectstatic
```

## 📞 Support

- **Documentation**: See the `/docs/` folder
- **Issues**: Create a GitHub issue
- **Email**: your-email@example.com

---

**Built with ❤️ using Django for freelancers and small businesses**

⭐ **Star this repo if you find it useful!**
