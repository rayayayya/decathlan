function showToast(title, message, type = 'normal', duration = 3000) {
    // Container utama
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'fixed bottom-4 right-4 z-50 flex flex-col gap-3';
        document.body.appendChild(container);
    }

    // Elemen toast
    const toast = document.createElement('div');
    toast.className = `
        flex items-start gap-3 px-4 py-3 rounded-xl shadow-lg border
        transform transition-all duration-300 translate-y-4 opacity-0
    `;

    // Gaya warna sesuai tipe
    if (type === 'success') {
        // Warna biru lembut untuk success
        toast.classList.add('bg-blue-50', 'border-blue-400', 'text-blue-700');
    } else if (type === 'error') {
        toast.classList.add('bg-red-50', 'border-red-400', 'text-red-700');
    } else {
        // Normal/info (abu kebiruan)
        toast.classList.add('bg-slate-50', 'border-blue-200', 'text-blue-800');
    }

    // Isi konten
    toast.innerHTML = `
        <div class="flex flex-col">
            <span class="font-semibold">${title}</span>
            <span class="text-sm">${message}</span>
        </div>
    `;

    // Masukkan ke container
    container.appendChild(toast);

    // Animasi masuk
    setTimeout(() => {
        toast.classList.remove('translate-y-4', 'opacity-0');
        toast.classList.add('translate-y-0', 'opacity-100');
    }, 50);

    // Animasi keluar
    setTimeout(() => {
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-4', 'opacity-0');
        setTimeout(() => toast.remove(), 300);
    }, duration);
}
