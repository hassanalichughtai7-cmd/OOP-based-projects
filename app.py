# --- FLASK AUR ZAROORI MODULES IMPORT KAR RAHE HAIN ---
from flask import Flask, render_template_string, request, session, redirect, url_for
import time

app = Flask(__name__)
app.secret_key = 'python_elite_luxury_2026_key'

# --- 50+ LUXURY ITEMS KI PYTHON LIST ---
PRODUCTS = [
    # WATCHES (Python Collection)
    {'id': 'w1', 'name': 'Rolex Submariner Gold', 'cat': 'Watch', 'price': 38500, 'img': 'https://images.unsplash.com/photo-1547996160-81dfa63595dd?w=500'},
    {'id': 'w2', 'name': 'Patek Philippe Nautilus', 'cat': 'Watch', 'price': 98000, 'img': 'https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=500'},
    {'id': 'w3', 'name': 'Audemars Piguet Royal Oak', 'cat': 'Watch', 'price': 54000, 'img': 'https://images.unsplash.com/photo-1539874754764-5a96559165b0?w=500'},
    {'id': 'w4', 'name': 'Cartier Santos Skeleton', 'cat': 'Watch', 'price': 28500, 'img': 'https://images.unsplash.com/photo-1614164185128-e4ec99c436d7?w=500'},
    {'id': 'w5', 'name': 'Hublot Big Bang Unico', 'cat': 'Watch', 'price': 24000, 'img': 'https://images.unsplash.com/photo-1526045431048-f857369aba09?w=500'},
    {'id': 'w6', 'name': 'Omega Speedmaster Moon', 'cat': 'Watch', 'price': 7400, 'img': 'https://images.unsplash.com/photo-1619134766035-61da3522736e?w=500'},
    {'id': 'w7', 'name': 'IWC Big Pilot Perpetual', 'cat': 'Watch', 'price': 32000, 'img': 'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=500'},
    {'id': 'w8', 'name': 'Breitling Navitimer B01', 'cat': 'Watch', 'price': 9200, 'img': 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=500'},
    {'id': 'w9', 'name': 'Zenith El Primero', 'cat': 'Watch', 'price': 8900, 'img': 'https://images.unsplash.com/photo-1508685096489-7aac29bb8b2a?w=500'},
    {'id': 'w10', 'name': 'Vacheron Overseas', 'cat': 'Watch', 'price': 45000, 'img': 'https://images.unsplash.com/photo-1612817159949-195b6eb9e31a?w=500'},
    
    # PERFUMES (Python Collection)
    {'id': 'p1', 'name': 'Dior Sauvage Elixir', 'cat': 'Perfume', 'price': 195, 'img': 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=500'},
    {'id': 'p2', 'name': 'Chanel No. 5 Parfum', 'cat': 'Perfume', 'price': 170, 'img': 'https://images.unsplash.com/photo-1523293182086-7651a899d37f?w=500'},
    {'id': 'p3', 'name': 'Tom Ford Ombré Leather', 'cat': 'Perfume', 'price': 220, 'img': 'https://images.unsplash.com/photo-1615485240384-552e4ec317d0?w=500'},
    {'id': 'p4', 'name': 'Creed Aventus', 'cat': 'Perfume', 'price': 445, 'img': 'https://images.unsplash.com/photo-1594035910387-fea47794261f?w=500'},
    {'id': 'p5', 'name': 'Baccarat Rouge 540', 'cat': 'Perfume', 'price': 340, 'img': 'https://images.unsplash.com/photo-1615485501062-b9187342674e?w=500'},
    {'id': 'p6', 'name': 'Versace Eros Flame', 'cat': 'Perfume', 'price': 125, 'img': 'https://images.unsplash.com/photo-1557170334-a9632e77c6e4?w=500'},
    {'id': 'p7', 'name': 'YSL Libre Intense', 'cat': 'Perfume', 'price': 160, 'img': 'https://images.unsplash.com/photo-1615485240905-188806209b0b?w=500'},
    {'id': 'p8', 'name': 'Armani Code Profumo', 'cat': 'Perfume', 'price': 140, 'img': 'https://images.unsplash.com/photo-1594035910387-fea47794261f?w=500'},
    {'id': 'p9', 'name': 'Hermes Terre d\'Hermes', 'cat': 'Perfume', 'price': 135, 'img': 'https://images.unsplash.com/photo-1594035910387-fea47794261f?w=500'},
    {'id': 'p10', 'name': 'Gucci Guilty Pour Homme', 'cat': 'Perfume', 'price': 110, 'img': 'https://images.unsplash.com/photo-1594035910387-fea47794261f?w=500'},

    # SHOES (Python Collection)
    {'id': 's1', 'name': 'Jordan 1 Chicago Retro', 'cat': 'Shoes', 'price': 1450, 'img': 'https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500'},
    {'id': 's2', 'name': 'Yeezy Boost 350 V2', 'cat': 'Shoes', 'price': 420, 'img': 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500'},
    {'id': 's3', 'name': 'Balenciaga Triple S', 'cat': 'Shoes', 'price': 1050, 'img': 'https://images.unsplash.com/photo-1582587319032-520427958133?w=500'},
    {'id': 's4', 'name': 'Hermès Paris Loafers', 'cat': 'Shoes', 'price': 1200, 'img': 'https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?w=500'},
    {'id': 's5', 'name': 'LV Trainer Sneaker', 'cat': 'Shoes', 'price': 1550, 'img': 'https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?w=500'},
    {'id': 's6', 'name': 'Prada Cloudbust Thunder', 'cat': 'Shoes', 'price': 920, 'img': 'https://images.unsplash.com/photo-1603808033192-082d6919d3e1?w=500'},
    {'id': 's7', 'name': 'Nike Off-White Presto', 'cat': 'Shoes', 'price': 1100, 'img': 'https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500'},
    {'id': 's8', 'name': 'Gucci Ace Sneakers', 'cat': 'Shoes', 'price': 790, 'img': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=500'},
    {'id': 's9', 'name': 'Adidas Human Race NMD', 'cat': 'Shoes', 'price': 850, 'img': 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500'},
    {'id': 's10', 'name': 'Louboutin Pik Boat', 'cat': 'Shoes', 'price': 950, 'img': 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500'},

    # BAGS (Python Collection)
    {'id': 'b1', 'name': 'Gucci Horsebit 1955', 'cat': 'Bags', 'price': 3100, 'img': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500'},
    {'id': 'b2', 'name': 'LV Keepall Bandoulière', 'cat': 'Bags', 'price': 2800, 'img': 'https://images.unsplash.com/photo-1547949003-9792a18a2601?w=500'},
    {'id': 'b3', 'name': 'Hermès Birkin 30 Gold', 'cat': 'Bags', 'price': 26500, 'img': 'https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?w=500'},
    {'id': 'b4', 'name': 'Chanel Classic Flap', 'cat': 'Bags', 'price': 9200, 'img': 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=500'},
    {'id': 'b5', 'name': 'Prada Re-Edition 2005', 'cat': 'Bags', 'price': 1950, 'img': 'https://images.unsplash.com/photo-1591561954557-26941169b49e?w=500'},
    {'id': 'b6', 'name': 'Fendi Peekaboo ISeeU', 'cat': 'Bags', 'price': 4600, 'img': 'https://images.unsplash.com/photo-1566150905458-1bf1fd113f0d?w=500'},
    {'id': 'b7', 'name': 'Dior Lady Dior Bag', 'cat': 'Bags', 'price': 5500, 'img': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500'},
    {'id': 'b8', 'name': 'YSL Sac De Jour', 'cat': 'Bags', 'price': 3200, 'img': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500'},
    {'id': 'b9', 'name': 'Celine Belt Bag', 'cat': 'Bags', 'price': 2400, 'img': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500'},
    {'id': 'b10', 'name': 'Bottega Veneta Cassette', 'cat': 'Bags', 'price': 3800, 'img': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500'},

    # JEWELRY (Python Collection)
    {'id': 'j1', 'name': 'Cartier Love Bracelet', 'cat': 'Jewelry', 'price': 7800, 'img': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=500'},
    {'id': 'j2', 'name': 'Tiffany Solitaire Ring', 'cat': 'Jewelry', 'price': 16500, 'img': 'https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=500'},
    {'id': 'j3', 'name': 'Bvlgari Serpenti Necklace', 'cat': 'Jewelry', 'price': 35000, 'img': 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=500'},
    {'id': 'j4', 'name': 'Van Cleef Alhambra', 'cat': 'Jewelry', 'price': 6950, 'img': 'https://images.unsplash.com/photo-1611652022419-a9419f74343d?w=500'},
    {'id': 'j5', 'name': 'Harry Winston Earrings', 'cat': 'Jewelry', 'price': 48000, 'img': 'https://images.unsplash.com/photo-1535632787350-4e68ef0ac584?w=500'},
    {'id': 'j6', 'name': 'Graff Diamond Brooch', 'cat': 'Jewelry', 'price': 22500, 'img': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500'},
    {'id': 'j7', 'name': 'Chopard Happy Hearts', 'cat': 'Jewelry', 'price': 3500, 'img': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=500'},
    {'id': 'j8', 'name': 'Mikimoto Pearl String', 'cat': 'Jewelry', 'price': 9800, 'img': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=500'},
    {'id': 'j9', 'name': 'Piaget Possession Ring', 'cat': 'Jewelry', 'price': 4200, 'img': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=500'},
    {'id': 'j10', 'name': 'Boucheron Quatre Cuff', 'cat': 'Jewelry', 'price': 12000, 'img': 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=500'},
    # Additional products to reach 50+
    {'id': 'w11', 'name': 'Zenith Chronomaster', 'cat': 'Watch', 'price': 11000, 'img': 'https://images.unsplash.com/photo-1547996160-81dfa63595dd?w=500'},
    {'id': 'p11', 'name': 'Roja Parfums Elysium', 'cat': 'Perfume', 'price': 300, 'img': 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=500'}
]

ADMIN_ID = "sheram123"
ADMIN_PASS = "123"
CUSTOMER_PASS = "786"

# --- HTML TEMPLATE (PYTHON BASED) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ELITE STORE | Python Edition 2026</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>

    <style>
        :root { --p-gold: #D4AF37; --p-dark: #0a0a0a; --p-gray: #151515; }
        body { font-family: 'Inter', sans-serif; background-color: var(--p-dark); color: white; overflow-x: hidden; }
        h1, .brand-logo { font-family: 'Playfair Display', serif; }
        .text-gold { color: var(--p-gold); }
        .ls-2 { letter-spacing: 2px; }

        #loginOverlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at center, #1a1a1a 0%, #000 100%); display: flex; align-items: center; justify-content: center; z-index: 10000; }
        .auth-card { background: var(--p-gray); border: 1px solid rgba(212, 175, 55, 0.2); border-radius: 30px; padding: 3.5rem 2rem; width: 100%; max-width: 420px; text-align: center; box-shadow: 0 40px 100px rgba(0,0,0,0.9); }
        .form-control-luxury { background: #000 !important; border: 1px solid #333 !important; color: white !important; border-radius: 15px; padding: 15px; text-align: center; margin-bottom: 1rem; width: 100%; }
        .btn-luxury { background: var(--p-gold); color: black; font-weight: 800; padding: 15px; border-radius: 15px; width: 100%; border: none; text-transform: uppercase; cursor: pointer; transition: 0.3s; }
        .btn-luxury:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(212, 175, 55, 0.3); }

        .navbar { background: rgba(10, 10, 10, 0.95); backdrop-filter: blur(15px); border-bottom: 1px solid rgba(212, 175, 55, 0.1); padding: 1rem 0; }
        .filter-pill { background: transparent; border: 1px solid #333; color: rgba(255,255,255,0.6); padding: 8px 22px; border-radius: 50px; margin: 0 5px; cursor: pointer; transition: 0.3s; }
        .filter-pill.active { background: var(--p-gold); color: black; border-color: var(--p-gold); }
        
        .product-card { background: #111; border: 1px solid #222; border-radius: 20px; overflow: hidden; transition: 0.4s; height: 100%; display: flex; flex-direction: column; }
        .product-card:hover { transform: translateY(-10px); border-color: var(--p-gold); box-shadow: 0 10px 30px rgba(212, 175, 55, 0.1); }
        .product-img-wrapper { height: 250px; overflow: hidden; position: relative; }
        .product-img { width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }
        .product-card:hover .product-img { transform: scale(1.1); }
        .btn-add { background: var(--p-gold); border: none; color: black; font-weight: 800; padding: 7px 18px; border-radius: 50px; font-size: 0.75rem; }
        
        #toast-container { position: fixed; bottom: 30px; right: 30px; z-index: 11000; }
        .luxury-toast { background: #222; border-left: 4px solid var(--p-gold); color: white; padding: 15px 25px; border-radius: 10px; margin-bottom: 10px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); font-weight: 600; }
        .admin-tag { background: #ff4d4d; color: white; font-size: 0.6rem; padding: 2px 6px; border-radius: 4px; font-weight: 900; margin-left: 5px; }
    </style>
</head>
<body>
    <div id="toast-container"></div>

    {% if not session.get('user') %}
    <!-- 1. PYTHON BACKEND LOGIN -->
    <div id="loginOverlay">
        <div class="auth-card animate__animated animate__fadeInDown">
            <h1 class="brand-logo mb-1 text-white">ELITE<span class="text-gold">STORE</span></h1>
            <p class="text-secondary mb-4 small text-uppercase">Luxury Portal (Python Powered)</p>
            <form action="/login" method="post">
                <input type="text" name="username" class="form-control-luxury" placeholder="Username / Admin ID" required>
                <input type="password" name="password" class="form-control-luxury" placeholder="Security Code" required>
                <button type="submit" class="btn-luxury">Log In</button>
            </form>
            <!-- Highlighted Login Details -->
            <div class="mt-4 p-3 border border-secondary rounded-4 small text-start">
                <div class="text-gold fw-bold mb-1">Login Details:</div>
                <div class="d-flex justify-content-between mb-1">
                    <span class="text-secondary fw-semibold">Admin ID:</span> <span class="text-white fw-bold">sheram123</span>
                </div>
                <div class="d-flex justify-content-between">
                    <span class="text-secondary fw-semibold">Admin Pass:</span> <span class="text-white fw-bold">123</span>
                </div>
                <hr class="my-2 border-secondary opacity-50">
                <div class="d-flex justify-content-between">
                    <span class="text-secondary fw-semibold">Customer Pass:</span> <span class="text-white fw-bold">786</span>
                </div>
            </div>
        </div>
    </div>
    {% else %}
    <!-- 2. MAIN PYTHON STORE UI -->
    <nav class="navbar sticky-top">
        <div class="container">
            <a href="/" class="brand-logo text-white text-decoration-none h3">ELITE<span class="text-gold">STORE</span></a>
            <div class="ms-auto d-flex align-items-center gap-3">
                <span class="text-secondary small d-none d-md-block">Swaagat hai, <span class="text-white fw-bold">{{ session['user'] }}</span>{% if session['role'] == 'admin' %}<span class="admin-tag">ADMIN</span>{% endif %}</span>
                <a href="/logout" class="btn btn-outline-secondary btn-sm rounded-pill px-3">Sign Out</a>
                <div class="position-relative" style="cursor:pointer" data-bs-toggle="offcanvas" data-bs-target="#cartBox">
                    <i class="bi bi-bag-heart text-white fs-3"></i>
                    <span id="cartCount" class="badge rounded-pill bg-warning text-dark position-absolute top-0 start-100 translate-middle" style="font-size:0.6rem">0</span>
                </div>
            </div>
        </div>
    </nav>

    <main class="container py-5">
        <section id="storeView">
            <header class="text-center mb-5 animate__animated animate__fadeIn">
                <h6 class="text-gold text-uppercase">Established 2026</h6>
                <h1 class="display-4 fw-bold">The Luxury <span class="text-gold">Edit</span></h1>
                <p class="text-secondary">Explore 50+ masterpieces in our Python-powered luxury catalog.</p>
            </header>

            <div class="d-flex justify-content-center overflow-auto pb-4 mb-4 no-scrollbar">
                <button class="filter-pill active" onclick="filter('All')">All Items</button>
                <button class="filter-pill" onclick="filter('Watch')">Watches</button>
                <button class="filter-pill" onclick="filter('Perfume')">Perfumes</button>
                <button class="filter-pill" onclick="filter('Shoes')">Shoes</button>
                <button class="filter-pill" onclick="filter('Bags')">Bags</button>
                <button class="filter-pill" onclick="filter('Jewelry')">Jewelry</button>
            </div>

            <div class="row g-4" id="productGrid">
                {% for p in products %}
                <div class="col-6 col-md-4 col-lg-3 product-item" data-cat="{{ p.cat }}">
                    <div class="product-card">
                        <div class="product-img-wrapper">
                            <img src="{{ p.img }}" class="product-img" loading="lazy" onerror="this.src='https://placehold.co/500x500/111/D4AF37?text={{p.name}}'">
                        </div>
                        <div class="p-3">
                            <span class="text-gold small fw-bold text-uppercase" style="font-size:0.6rem">{{ p.cat }}</span>
                            <h6 class="mt-1 mb-3 text-truncate">{{ p.name }}</h6>
                            <div class="d-flex justify-content-between align-items-center">
                                <span class="fw-bold text-white small">${{ "{:,}".format(p.price) }}</span>
                                {% if session['role'] == 'customer' %}
                                <button class="btn-add" onclick="addToBag('{{ p.name }}', {{ p.price }})">ADD</button>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>
        
        {% if session['role'] == 'admin' %}
        <section id="adminView" class="mt-5 border-top border-secondary pt-5">
            <div class="row">
                <div class="col-lg-4 mb-4">
                    <div class="auth-card w-100 p-4 text-start">
                        <h4 class="text-gold brand-logo mb-4">Add New Products</h4>
                        <form action="/add" method="post">
                            <label class="small text-secondary mb-1">Items Name</label>
                            <input type="text" name="name" class="form-control-luxury text-start" required>
                            <label class="small text-secondary mb-1">Select Categories</label>
                            <select name="cat" class="form-control-luxury text-start">
                                <option>Watch</option><option>Perfume</option><option>Shoes</option><option>Bags</option><option>Jewelry</option>
                            </select>
                            <label class="small text-secondary mb-1">Price ($)</label>
                            <input type="number" name="price" class="form-control-luxury text-start" required>
                            <label class="small text-secondary mb-1">Image URL</label>
                            <input type="text" name="img" class="form-control-luxury text-start">
                            <button type="submit" class="btn-luxury">Save Into Inventory</button>
                        </form>
                    </div>
                </div>
            </div>
        </section>
        {% endif %}
    </main>

    <!-- PYTHON POWERED BAG SIDEBAR -->
    <div class="offcanvas offcanvas-end bg-dark text-white" id="cartBox" style="width: 350px;">
        <div class="offcanvas-header border-bottom border-secondary p-4">
            <h5 class="offcanvas-title fw-bold">Shopping Bag</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas"></button>
        </div>
        <div class="offcanvas-body p-4">
            <div id="cartList"></div>
        </div>
        <div class="offcanvas-footer p-4 border-top border-secondary">
            <div class="d-flex justify-content-between mb-4 h5">
                <span>Total:</span><span class="text-gold" id="totalPrice">$0.00</span>
            </div>
            <button class="btn-luxury" onclick="confirmOrder()">Complete Transaction</button>
        </div>
    </div>
    {% endif %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        let cart = [];
        function notify(msg) {
            const cont = document.getElementById('toast-container');
            const t = document.createElement('div');
            t.className = 'luxury-toast animate__animated animate__fadeInRight';
            t.innerHTML = `<span>${msg}</span>`;
            cont.appendChild(t);
            setTimeout(() => t.remove(), 3000);
        }

        function addToBag(name, price) {
            cart.push({name, price});
            updateUI();
            notify(`${name} Added`);
        }

        function updateUI() {
            document.getElementById('cartCount').innerText = cart.length;
            let total = 0;
            const list = document.getElementById('cartList');
            list.innerHTML = cart.map((item) => {
                total += item.price;
                return `<div class="d-flex justify-content-between mb-3 pb-2 border-bottom border-secondary" style="font-size:0.9rem">
                            <span>${item.name}</span>
                            <span class="text-gold">$${item.price.toLocaleString()}</span>
                        </div>`;
            }).join('');
            document.getElementById('totalPrice').innerText = `$${total.toLocaleString()}`;
        }

        function confirmOrder() {
            if(cart.length === 0) return;
            cart = [];
            updateUI();
            notify("Order Confirmed");
        }

        function filter(cat) {
            document.querySelectorAll('.filter-pill').forEach(b => b.classList.remove('active'));
            if (event) event.target.classList.add('active');
            document.querySelectorAll('.product-item').forEach(item => {
                if(cat === 'All' || item.getAttribute('data-cat') === cat) item.style.display = 'block';
                else item.style.display = 'none';
            });
        }
    </script>
</body>
</html>
"""

# --- PYTHON ROUTES (FLASK LOGIC) ---

@app.route('/')
def index():
    # Python backend index render kar raha hai
    return render_template_string(HTML_TEMPLATE, products=PRODUCTS)

@app.route('/login', methods=['POST'])
def login():
    # Python logic login handle kar rahi hai
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == ADMIN_ID and password == ADMIN_PASS:
        session['user'] = username
        session['role'] = 'admin'
    elif password == CUSTOMER_PASS:
        session['user'] = username if username else "Elite Guest"
        session['role'] = 'customer'
    
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Session clear kar rahe hain (Python control)
    session.clear()
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_product():
    # Admin ke liye naya product add karne ki Python logic
    if session.get('role') == 'admin':
        try:
            new_item = {
                'id': str(time.time()),
                'name': request.form.get('name'),
                'cat': request.form.get('cat'),
                'price': int(request.form.get('price')),
                'img': request.form.get('img') if request.form.get('img') else 'https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=500'
            }
            PRODUCTS.insert(0, new_item)
        except:
            pass
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Python server start ho raha hai
    # debug=True se error detect karna aasan hota hai
    app.run(debug=True)