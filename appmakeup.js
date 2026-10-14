// Mock Data: 20 Products
const products = [
    { id: 1, name: "Son Romand Juicy Lasting Tint", brand: "Romand", category: "Son môi", price: 129000, oldPrice: 199000, discount: 35, rating: 4.9, sold: 1200, image: "https://images.unsplash.com/photo-1586495777744-4413f21062fa?auto=format&fit=crop&w=400&q=80", description: "Son tint bóng ngọt ngào, giữ màu lâu trôi." },
    { id: 2, name: "Kem nền Maybelline Fit Me Matte", brand: "Maybelline", category: "Kem nền", price: 185000, oldPrice: 220000, discount: 16, rating: 4.8, sold: 3400, image: "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?auto=format&fit=crop&w=400&q=80", description: "Kem nền kiềm dầu, che phủ tốt phù hợp da mụn." },
    { id: 3, name: "Cushion Clio Kill Cover", brand: "Clio", category: "Cushion", price: 450000, oldPrice: 650000, discount: 30, rating: 4.7, sold: 890, image: "https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=400&q=80", description: "Phấn nước che phủ hoàn hảo, bền màu 48h." },
    { id: 4, name: "Sữa rửa mặt CeraVe Hydrating", brand: "CeraVe", category: "Chăm sóc da", price: 350000, oldPrice: 420000, discount: 17, rating: 4.9, sold: 5600, image: "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?auto=format&fit=crop&w=400&q=80", description: "Sữa rửa mặt dưỡng ẩm dành cho da thường đến da khô." },
    { id: 5, name: "Toner La Roche-Posay Effaclar", brand: "La Roche-Posay", category: "Chăm sóc da", price: 380000, oldPrice: 450000, discount: 15, rating: 4.8, sold: 2100, image: "https://images.unsplash.com/photo-1611078580665-27a3c751cb68?auto=format&fit=crop&w=400&q=80", description: "Nước hoa hồng dành riêng cho da dầu mụn." },
    { id: 6, name: "Serum The Ordinary Niacinamide 10%", brand: "The Ordinary", category: "Chăm sóc da", price: 210000, oldPrice: 280000, discount: 25, rating: 4.6, sold: 8900, image: "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=400&q=80", description: "Tinh chất mờ thâm mụn, kiểm soát bã nhờn." },
    { id: 7, name: "Kem chống nắng Anessa Perfect UV", brand: "Anessa", category: "Chống nắng", price: 495000, oldPrice: 685000, discount: 28, rating: 4.9, sold: 4500, image: "https://images.unsplash.com/photo-1556228720-1c27bef8f219?auto=format&fit=crop&w=400&q=80", description: "Sữa chống nắng bảo vệ tối ưu, kiềm dầu tốt." },
    { id: 8, name: "Son dưỡng Dior Addict Lip Glow", brand: "Dior", category: "Son môi", price: 850000, oldPrice: 950000, discount: 10, rating: 4.9, sold: 1500, image: "https://images.unsplash.com/photo-1617220556247-497d52c7943d?auto=format&fit=crop&w=400&q=80", description: "Son dưỡng có màu tự nhiên, căng mọng đôi môi." },
    { id: 9, name: "Dầu gội TRESemmé Keratin Smooth", brand: "TRESemmé", category: "Chăm sóc tóc", price: 155000, oldPrice: 199000, discount: 22, rating: 4.5, sold: 3200, image: "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?auto=format&fit=crop&w=400&q=80", description: "Dầu gội dưỡng tóc suôn mượt vào nếp." },
    { id: 10, name: "Nước hoa Chanel Coco Mademoiselle", brand: "Chanel", category: "Nước hoa", price: 3500000, oldPrice: 3800000, discount: 8, rating: 5.0, sold: 450, image: "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=400&q=80", description: "Hương thơm sang trọng, quyến rũ và nữ tính." },
    { id: 11, name: "Phấn má hồng MAC Powder Blush", brand: "MAC", category: "Má hồng", price: 590000, oldPrice: 700000, discount: 15, rating: 4.7, sold: 1100, image: "https://images.unsplash.com/photo-1512496015851-a1fa5cb91aad?auto=format&fit=crop&w=400&q=80", description: "Phấn má hồng lên màu chuẩn, mịn lì." },
    { id: 12, name: "Bảng phấn mắt 3CE Multi Eye Color", brand: "3CE", category: "Phấn mắt", price: 750000, oldPrice: 890000, discount: 16, rating: 4.8, sold: 1800, image: "https://images.unsplash.com/photo-1583241475880-083f84372725?auto=format&fit=crop&w=400&q=80", description: "Bảng phấn mắt 9 màu thời thượng, dễ phối." },
    { id: 13, name: "Mascara Maybelline Lash Sensational", brand: "Maybelline", category: "Trang điểm", price: 165000, oldPrice: 200000, discount: 17, rating: 4.6, sold: 2800, image: "https://images.unsplash.com/photo-1587778082149-bd5b1bf5d3f8?auto=format&fit=crop&w=400&q=80", description: "Mascara làm cong và dày mi hiệu quả." },
    { id: 14, name: "Kẻ mắt nước Kiss Me Heroine", brand: "Kiss Me", category: "Trang điểm", price: 250000, oldPrice: 300000, discount: 16, rating: 4.9, sold: 3100, image: "https://images.unsplash.com/photo-1596755389378-c5b96796fa2c?auto=format&fit=crop&w=400&q=80", description: "Kẻ mắt siêu lì, không lem không trôi." },
    { id: 15, name: "Kem dưỡng ẩm Neutrogena Hydro Boost", brand: "Neutrogena", category: "Chăm sóc da", price: 320000, oldPrice: 450000, discount: 28, rating: 4.8, sold: 5000, image: "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?auto=format&fit=crop&w=400&q=80", description: "Kem dưỡng cấp nước dạng gel mát lạnh." },
    { id: 16, name: "Mặt nạ Mediheal Teatree Care", brand: "Mediheal", category: "Chăm sóc da", price: 25000, oldPrice: 35000, discount: 28, rating: 4.7, sold: 15000, image: "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=400&q=80", description: "Mặt nạ tràm trà giảm sưng mụn, làm dịu da." },
    { id: 17, name: "Sữa tắm Love Beauty And Planet", brand: "Love Beauty And Planet", category: "Body", price: 145000, oldPrice: 180000, discount: 19, rating: 4.5, sold: 2200, image: "https://images.unsplash.com/photo-1584949514122-f6734fbce994?auto=format&fit=crop&w=400&q=80", description: "Sữa tắm thuần chay hương hoa hồng." },
    { id: 18, name: "Body Lotion Paula's Choice 2% BHA", brand: "Paula's Choice", category: "Body", price: 850000, oldPrice: 950000, discount: 10, rating: 4.8, sold: 950, image: "https://images.unsplash.com/photo-1620916297397-a4a5402a3c6c?auto=format&fit=crop&w=400&q=80", description: "Dưỡng thể loại bỏ tế bào chết, mờ thâm mụn lưng." },
    { id: 19, name: "Son kem MAC Powder Kiss Liquid", brand: "MAC", category: "Son môi", price: 680000, oldPrice: 750000, discount: 9, rating: 4.7, sold: 1600, image: "https://images.unsplash.com/photo-1599305090598-fe179d501227?auto=format&fit=crop&w=400&q=80", description: "Son kem lì mịn màng, ẩm mượt." },
    { id: 20, name: "Nước tẩy trang Bioderma Sensibio H2O", brand: "Bioderma", category: "Chăm sóc da", price: 395000, oldPrice: 495000, discount: 20, rating: 4.9, sold: 7500, image: "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?auto=format&fit=crop&w=400&q=80", description: "Tẩy trang dịu nhẹ cho da nhạy cảm." }
];

// Banners
const banners = [
    { image: "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?auto=format&fit=crop&w=1200&q=80", title: "SALE ĐẾN 50%", text: "Beauty deals dành riêng cho bạn." },
    { image: "https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=1200&q=80", title: "MỸ PHẨM HOT", text: "Khám phá xu hướng làm đẹp mới nhất." },
    { image: "https://images.unsplash.com/photo-1512496015851-a1fa5cb91aad?auto=format&fit=crop&w=1200&q=80", title: "DEAL HÔM NAY", text: "Ưu đãi giới hạn, mua ngay kẻo lỡ!" }
];

// State
let cart = JSON.parse(localStorage.getItem('cart')) || [];
let wishlist = JSON.parse(localStorage.getItem('wishlist')) || [];
let currentFilter = { category: 'Tất cả', price: 'all', rating: 'all', sort: 'default', search: '' };

// Format Currency
const formatMoney = (amount) => {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(amount);
};

// Utilities
const saveToLocalStorage = () => {
    localStorage.setItem('cart', JSON.stringify(cart));
    localStorage.setItem('wishlist', JSON.stringify(wishlist));
    updateBadges();
};

const showToast = (message, type = 'success') => {
    const toastContainer = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = 'toast';
    
    let icon = type === 'success' ? '<i class="fas fa-check-circle" style="color:#2ecc71;"></i>' : 
              (type === 'heart' ? '<i class="fas fa-heart" style="color:#ff6b81;"></i>' : '<i class="fas fa-info-circle" style="color:#3498db;"></i>');
              
    toast.innerHTML = `${icon} <span>${message}</span>`;
    toastContainer.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s forwards';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
};

// Render Products
const renderProductCard = (product) => {
    const isWishlist = wishlist.includes(product.id);
    return `
        <div class="product-card" data-id="${product.id}">
            <div class="product-badge">-${product.discount}%</div>
            <button class="product-wishlist ${isWishlist ? 'active' : ''}" onclick="toggleWishlist(event, ${product.id})">
                <i class="${isWishlist ? 'fas' : 'far'} fa-heart"></i>
            </button>
            <img src="${product.image}" alt="${product.name}" class="product-img" onclick="openProductModal(${product.id})">
            <div class="product-info">
                <div class="product-brand">${product.brand}</div>
                <div class="product-name" onclick="openProductModal(${product.id})">${product.name}</div>
                <div class="product-rating">
                    ${'★'.repeat(Math.floor(product.rating))}${product.rating % 1 !== 0 ? '½' : ''}
                    <span>(${product.rating})</span>
                </div>
                <div class="product-price-row">
                    <span class="product-price">${formatMoney(product.price)}</span>
                    <span class="product-old-price">${formatMoney(product.oldPrice)}</span>
                </div>
                <div class="product-sold">Đã bán ${product.sold > 1000 ? (product.sold/1000).toFixed(1) + 'k' : product.sold}</div>
                <button class="add-to-cart-btn" onclick="addToCart(${product.id})">
                    + Thêm vào giỏ
                </button>
            </div>
        </div>
    `;
};

const renderMainProducts = () => {
    let filtered = products.filter(p => {
        // Search
        if (currentFilter.search && !p.name.toLowerCase().includes(currentFilter.search.toLowerCase()) && !p.brand.toLowerCase().includes(currentFilter.search.toLowerCase())) return false;
        
        // Category
        if (currentFilter.category !== 'Tất cả' && p.category !== currentFilter.category) return false;
        
        // Price
        if (currentFilter.price === 'under100' && p.price >= 100000) return false;
        if (currentFilter.price === '100to300' && (p.price < 100000 || p.price > 300000)) return false;
        if (currentFilter.price === '300to500' && (p.price < 300000 || p.price > 500000)) return false;
        if (currentFilter.price === 'above500' && p.price <= 500000) return false;
        
        // Rating
        if (currentFilter.rating !== 'all' && p.rating < parseFloat(currentFilter.rating)) return false;
        
        return true;
    });

    // Sort
    if (currentFilter.sort === 'price-asc') filtered.sort((a, b) => a.price - b.price);
    else if (currentFilter.sort === 'price-desc') filtered.sort((a, b) => b.price - a.price);
    else if (currentFilter.sort === 'best-seller') filtered.sort((a, b) => b.sold - a.sold);
    else if (currentFilter.sort === 'rating') filtered.sort((a, b) => b.rating - a.rating);
    else if (currentFilter.sort === 'discount') filtered.sort((a, b) => b.discount - a.discount);

    const container = document.getElementById('main-products');
    const msg = document.getElementById('no-products-msg');
    
    if (filtered.length === 0) {
        container.innerHTML = '';
        msg.classList.remove('hidden');
    } else {
        msg.classList.add('hidden');
        container.innerHTML = filtered.map(renderProductCard).join('');
    }
};

const renderFlashSale = () => {
    const flashProducts = [...products].sort((a, b) => b.discount - a.discount).slice(0, 8);
    document.getElementById('flash-sale-products').innerHTML = flashProducts.map(renderProductCard).join('');
};

// Wishlist Logic
const toggleWishlist = (event, id) => {
    event.stopPropagation();
    const index = wishlist.indexOf(id);
    const btn = event.currentTarget;
    const icon = btn.querySelector('i');
    
    const product = products.find(p => p.id === id);
    
    if (index === -1) {
        wishlist.push(id);
        btn.classList.add('active');
        icon.classList.remove('far');
        icon.classList.add('fas');
        showToast(`Đã thêm ${product.name} vào yêu thích`, 'heart');
    } else {
        wishlist.splice(index, 1);
        btn.classList.remove('active');
        icon.classList.add('far');
        icon.classList.remove('fas');
        showToast(`Đã bỏ yêu thích ${product.name}`, 'info');
    }
    
    saveToLocalStorage();
    
    // Also re-render main products to keep heart states consistent if filtering
    if(document.getElementById('product-modal').classList.contains('active')) {
        // If modal open, update its heart button too
        const modalHeart = document.getElementById('modal-heart-btn');
        if(modalHeart) {
            modalHeart.innerHTML = wishlist.includes(id) ? '<i class="fas fa-heart"></i> Đã yêu thích' : '<i class="far fa-heart"></i> Yêu thích';
        }
    }
};

// Cart Logic
const addToCart = (id, qty = 1) => {
    const product = products.find(p => p.id === id);
    const existing = cart.find(item => item.id === id);
    
    if (existing) {
        existing.qty += qty;
    } else {
        cart.push({ ...product, qty });
    }
    
    saveToLocalStorage();
    renderCart();
    showToast(`Đã thêm ${product.name} vào giỏ hàng`);
};

const updateCartQty = (id, change) => {
    const item = cart.find(i => i.id === id);
    if (item) {
        item.qty += change;
        if (item.qty <= 0) {
            cart = cart.filter(i => i.id !== id);
        }
        saveToLocalStorage();
        renderCart();
    }
};

const removeFromCart = (id) => {
    cart = cart.filter(i => i.id !== id);
    saveToLocalStorage();
    renderCart();
    showToast(`Đã xóa sản phẩm khỏi giỏ hàng`, 'info');
};

let appliedDiscount = 0;
const renderCart = () => {
    const container = document.getElementById('cart-items');
    
    if (cart.length === 0) {
        container.innerHTML = '<div style="text-align:center; padding: 50px 0; color: #747d8c;">Giỏ hàng trống</div>';
    } else {
        container.innerHTML = cart.map(item => `
            <div class="cart-item">
                <img src="${item.image}" class="cart-item-img" alt="${item.name}">
                <div class="cart-item-info">
                    <div class="cart-item-title">${item.name}</div>
                    <div class="cart-item-price">${formatMoney(item.price)}</div>
                    <div class="cart-item-actions">
                        <div class="detail-qty" style="margin:0; gap:5px;">
                            <button class="qty-btn" onclick="updateCartQty(${item.id}, -1)">-</button>
                            <input class="qty-input" style="width:30px; border:none;" type="text" value="${item.qty}" readonly>
                            <button class="qty-btn" onclick="updateCartQty(${item.id}, 1)">+</button>
                        </div>
                        <button class="remove-btn" onclick="removeFromCart(${item.id})"><i class="fas fa-trash"></i></button>
                    </div>
                </div>
            </div>
        `).join('');
    }
    
    // Calculate Totals
    const subtotal = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
    const shipping = cart.length > 0 ? 20000 : 0;
    
    document.getElementById('subtotal').innerText = formatMoney(subtotal);
    document.getElementById('shipping-fee').innerText = formatMoney(shipping);
    
    if (appliedDiscount > 0 && cart.length > 0) {
        const discountVal = (subtotal * appliedDiscount) / 100;
        document.getElementById('discount-row').style.display = 'flex';
        document.getElementById('discount-amount').innerText = `-${formatMoney(discountVal)}`;
        document.getElementById('total-price').innerText = formatMoney(subtotal - discountVal + shipping);
    } else {
        document.getElementById('discount-row').style.display = 'none';
        document.getElementById('total-price').innerText = formatMoney(subtotal + shipping);
        appliedDiscount = 0; // reset
    }
};

const updateBadges = () => {
    const cartQty = cart.reduce((sum, item) => sum + item.qty, 0);
    document.getElementById('cart-badge').innerText = cartQty;
    document.getElementById('wishlist-badge').innerText = wishlist.length;
};

// UI Interactions
const openModal = (id) => {
    document.getElementById(id).classList.add('active');
    document.getElementById('cart-overlay').classList.add('active'); // Reusing overlay
};

const closeModal = (id) => {
    document.getElementById(id).classList.remove('active');
    document.getElementById('cart-overlay').classList.remove('active');
};

const openProductModal = (id) => {
    const product = products.find(p => p.id === id);
    const isWishlist = wishlist.includes(product.id);
    const container = document.getElementById('product-detail-content');
    
    container.innerHTML = `
        <img src="${product.image}" alt="${product.name}" class="detail-img">
        <div class="detail-info">
            <div class="detail-brand">${product.brand}</div>
            <div class="detail-name">${product.name}</div>
            <div class="product-rating" style="margin-bottom: 20px;">
                ${'★'.repeat(Math.floor(product.rating))}${product.rating % 1 !== 0 ? '½' : ''}
                <span>(${product.rating}) | Đã bán ${product.sold}</span>
            </div>
            <div class="detail-price-row">
                <span class="detail-price">${formatMoney(product.price)}</span>
                <span class="product-old-price">${formatMoney(product.oldPrice)}</span>
                <span class="product-badge" style="position:static;">-${product.discount}%</span>
            </div>
            <div class="detail-desc">
                ${product.description} <br><br>
                Sản phẩm chính hãng 100%. Đổi trả trong vòng 7 ngày nếu có lỗi từ nhà sản xuất.
            </div>
            <div class="detail-qty">
                <span>Số lượng:</span>
                <button class="qty-btn" id="modal-qty-minus">-</button>
                <input type="text" class="qty-input" id="modal-qty-input" value="1" readonly>
                <button class="qty-btn" id="modal-qty-plus">+</button>
            </div>
            <div class="detail-actions">
                <button class="btn-outline" id="modal-add-cart">Thêm vào giỏ</button>
                <button class="btn-primary" id="modal-buy-now">Mua ngay</button>
            </div>
            ${product.category === 'Son môi' ? `<button class="btn-primary" style="margin-top:15px; width:100%; background: linear-gradient(45deg, #ff6b81, #ff4757);" id="modal-vto-btn"><i class="fas fa-camera"></i> Thử trên khuôn mặt bạn</button>` : ''}
            
            <!-- Affiliate Links -->
            <div class="affiliate-links" style="margin-top: 15px;">
                <p style="font-size: 0.85rem; color: var(--text-light); margin-bottom: 8px;">Hoặc mua chính hãng tại:</p>
                <div style="display: flex; gap: 10px;">
                    <a href="https://shopee.vn/" target="_blank" class="btn-affiliate shopee">
                        Shopee
                    </a>
                    <a href="https://www.lazada.vn/" target="_blank" class="btn-affiliate lazada">
                        Lazada
                    </a>
                    <a href="https://www.tiktok.com/" target="_blank" class="btn-affiliate tiktok">
                        TikTok
                    </a>
                </div>
            </div>

            <button class="btn-outline" style="margin-top:15px; width:100%;" id="modal-heart-btn" onclick="toggleWishlist(event, ${product.id})">
                <i class="${isWishlist ? 'fas' : 'far'} fa-heart"></i> ${isWishlist ? 'Đã yêu thích' : 'Yêu thích'}
            </button>
        </div>
    `;
    
    openModal('product-modal');
    
    // Quantity logic
    let qty = 1;
    const qtyInput = document.getElementById('modal-qty-input');
    document.getElementById('modal-qty-minus').onclick = () => { if(qty > 1) { qty--; qtyInput.value = qty; } };
    document.getElementById('modal-qty-plus').onclick = () => { qty++; qtyInput.value = qty; };
    
    document.getElementById('modal-add-cart').onclick = () => {
        addToCart(product.id, qty);
        closeModal('product-modal');
    };
    
    document.getElementById('modal-buy-now').onclick = () => {
        addToCart(product.id, qty);
        closeModal('product-modal');
        document.getElementById('cart-drawer').classList.add('active');
        document.getElementById('cart-overlay').classList.add('active');
    };

    const vtoBtn = document.getElementById('modal-vto-btn');
    if (vtoBtn) {
        vtoBtn.onclick = () => {
            closeModal('product-modal');
            openVTO(product);
        };
    }
};

// VTO (Virtual Try-On) Logic
let vtoStream = null;

const openVTO = async (product) => {
    openModal('vto-modal');
    const video = document.getElementById('vto-video');
    const overlay = document.getElementById('vto-overlay');
    
    // Reset overlay
    overlay.style.backgroundColor = 'transparent';
    document.querySelectorAll('.vto-swatch').forEach(s => s.classList.remove('active'));
    
    try {
        vtoStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } });
        video.srcObject = vtoStream;
    } catch (err) {
        alert('Không thể truy cập Camera. Vui lòng cấp quyền hoặc thử lại trên thiết bị khác.');
        closeModal('vto-modal');
    }

    document.getElementById('vto-add-cart-btn').onclick = () => {
        addToCart(product.id, 1);
        closeVTOModal();
        document.getElementById('cart-drawer').classList.add('active');
        document.getElementById('cart-overlay').classList.add('active');
    };
};

const closeVTOModal = () => {
    closeModal('vto-modal');
    if (vtoStream) {
        vtoStream.getTracks().forEach(track => track.stop());
        vtoStream = null;
    }
};

// Event Listeners Setup
const setupEventListeners = () => {
    // Cart & Overlay
    document.getElementById('cart-btn').addEventListener('click', () => {
        document.getElementById('cart-drawer').classList.add('active');
        document.getElementById('cart-overlay').classList.add('active');
    });
    
    document.getElementById('close-cart').addEventListener('click', () => {
        document.getElementById('cart-drawer').classList.remove('active');
        document.getElementById('cart-overlay').classList.remove('active');
    });
    
    document.getElementById('cart-overlay').addEventListener('click', () => {
        document.getElementById('cart-drawer').classList.remove('active');
        document.querySelectorAll('.modal').forEach(m => m.classList.remove('active'));
        document.getElementById('cart-overlay').classList.remove('active');
    });

    // Filters
    const radios = document.querySelectorAll('.sidebar input[type="radio"]');
    radios.forEach(radio => {
        radio.addEventListener('change', (e) => {
            currentFilter[e.target.name] = e.target.value;
            renderMainProducts();
        });
    });

    // Sort
    document.getElementById('sort-select').addEventListener('change', (e) => {
        currentFilter.sort = e.target.value;
        renderMainProducts();
    });

    // Search
    const performSearch = () => {
        currentFilter.search = document.getElementById('search-input').value;
        renderMainProducts();
        document.getElementById('categories').scrollIntoView({behavior: 'smooth'});
    };
    document.getElementById('search-btn').addEventListener('click', performSearch);
    document.getElementById('search-input').addEventListener('keypress', (e) => {
        if(e.key === 'Enter') performSearch();
    });

    // Promo Code
    document.getElementById('apply-promo').addEventListener('click', () => {
        const code = document.getElementById('promo-input').value.trim().toUpperCase();
        const msgBox = document.getElementById('promo-msg');
        if (['BEAUTY10', 'SALE20', 'WELCOME50'].includes(code)) {
            let discount = parseInt(code.replace(/[A-Z]/g, ''));
            appliedDiscount = discount;
            msgBox.innerHTML = `<span class="promo-success">Đã áp dụng giảm ${discount}%</span>`;
            renderCart();
        } else {
            msgBox.innerHTML = `<span class="promo-error">Mã không hợp lệ</span>`;
            appliedDiscount = 0;
            renderCart();
        }
    });

    // Categories grid click
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('click', () => {
            const cat = card.getAttribute('data-cat');
            const radio = document.querySelector(`input[name="category"][value="${cat}"]`);
            if (radio) radio.checked = true;
            currentFilter.category = cat;
            renderMainProducts();
            document.querySelector('.main-layout').scrollIntoView({behavior: 'smooth'});
        });
    });

    // VTO Swatches & Actions
    document.querySelectorAll('.vto-swatch').forEach(swatch => {
        swatch.addEventListener('click', () => {
            document.querySelectorAll('.vto-swatch').forEach(s => s.classList.remove('active'));
            swatch.classList.add('active');
            const color = swatch.getAttribute('data-color');
            document.getElementById('vto-overlay').style.backgroundColor = color;
        });
    });

    document.getElementById('vto-capture-btn').addEventListener('click', () => {
        const video = document.getElementById('vto-video');
        const canvas = document.getElementById('vto-canvas');
        const overlay = document.getElementById('vto-overlay');
        
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext('2d');
        
        // Draw video (mirrored)
        ctx.translate(canvas.width, 0);
        ctx.scale(-1, 1);
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        // Reset transform to draw overlay
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        
        // Draw tinted overlay
        ctx.fillStyle = overlay.style.backgroundColor || 'transparent';
        ctx.globalCompositeOperation = "multiply";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Download image
        const dataUrl = canvas.toDataURL('image/png');
        const a = document.createElement('a');
        a.href = dataUrl;
        a.download = 'beauty-store-try-on.png';
        a.click();
        
        showToast('Đã lưu ảnh chụp vào máy!', 'success');
    });

    document.getElementById('close-vto-modal').addEventListener('click', closeVTOModal);

    // Modals Close
    document.querySelectorAll('.close-modal').forEach(btn => {
        if(btn.id === 'close-vto-modal') return; // Handled separately
        btn.addEventListener('click', () => {
            btn.closest('.modal').classList.remove('active');
            document.getElementById('cart-overlay').classList.remove('active');
        });
    });

    // Checkout
    document.getElementById('checkout-btn').addEventListener('click', () => {
        if (cart.length === 0) return showToast('Giỏ hàng trống!', 'error');
        document.getElementById('cart-drawer').classList.remove('active');
        openModal('checkout-modal');
    });

    document.getElementById('checkout-form').addEventListener('submit', (e) => {
        e.preventDefault();
        cart = []; // clear cart
        saveToLocalStorage();
        renderCart();
        closeModal('checkout-modal');
        openModal('success-modal');
    });

    document.getElementById('continue-shopping').addEventListener('click', () => {
        closeModal('success-modal');
    });
};

// Flash Sale Timer
const startTimer = () => {
    let timeInSecs = 2 * 3600 + 15 * 60 + 43; // 02:15:43
    const timerBoxes = document.querySelectorAll('.time-box');
    
    setInterval(() => {
        timeInSecs--;
        if (timeInSecs < 0) timeInSecs = 24 * 3600; // Reset just for demo
        
        let h = Math.floor(timeInSecs / 3600);
        let m = Math.floor((timeInSecs % 3600) / 60);
        let s = timeInSecs % 60;
        
        timerBoxes[0].innerText = h.toString().padStart(2, '0');
        timerBoxes[1].innerText = m.toString().padStart(2, '0');
        timerBoxes[2].innerText = s.toString().padStart(2, '0');
    }, 1000);
};

// Hero Carousel
const initCarousel = () => {
    const container = document.getElementById('hero-carousel');
    const indicatorsContainer = document.getElementById('carousel-indicators');
    
    container.innerHTML = banners.map(b => `
        <div class="banner-slide" style="background-image: url('${b.image}')">
            <div class="banner-content">
                <h2>${b.title}</h2>
                <p>${b.text}</p>
                <a href="#categories" class="banner-btn">XEM NGAY</a>
            </div>
        </div>
    `).join('');
    
    indicatorsContainer.innerHTML = banners.map((_, i) => `
        <div class="indicator ${i === 0 ? 'active' : ''}" data-index="${i}"></div>
    `).join('');
    
    let currentIndex = 0;
    const slidesCount = banners.length;
    
    const goToSlide = (index) => {
        if(index < 0) index = slidesCount - 1;
        if(index >= slidesCount) index = 0;
        currentIndex = index;
        
        container.style.transform = `translateX(-${currentIndex * 100}%)`;
        
        document.querySelectorAll('.indicator').forEach((ind, i) => {
            ind.classList.toggle('active', i === currentIndex);
        });
    };
    
    document.getElementById('carousel-prev').onclick = () => goToSlide(currentIndex - 1);
    document.getElementById('carousel-next').onclick = () => goToSlide(currentIndex + 1);
    
    document.querySelectorAll('.indicator').forEach(ind => {
        ind.onclick = () => goToSlide(parseInt(ind.getAttribute('data-index')));
    });
    
    setInterval(() => goToSlide(currentIndex + 1), 5000);
};

// Init
document.addEventListener('DOMContentLoaded', () => {
    initCarousel();
    renderFlashSale();
    renderMainProducts();
    renderCart();
    updateBadges();
    setupEventListeners();
    startTimer();
});
