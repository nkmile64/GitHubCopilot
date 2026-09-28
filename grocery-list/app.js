const STORAGE_KEY = 'groceryItems_v1'
let items = []
let editingId = null

const $ = id => document.getElementById(id)
const save = () => localStorage.setItem(STORAGE_KEY, JSON.stringify(items))
const load = () => { try { items = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [] } catch (e) { items = [] } }

function render(filter = '') {
    const body = $('itemsBody')
    body.innerHTML = ''
    const filtered = items.filter(i => (i.name + '' + i.category).toLowerCase().includes(filter.toLowerCase()))
    if (!filtered.length) { $('emptyNotice').style.display = 'block'; $('itemsTable').style.display = 'none'; return }
    $('emptyNotice').style.display = 'none'; $('itemsTable').style.display = 'table'
    filtered.forEach(it => {
        const tr = document.createElement('tr')
        tr.innerHTML = `
      <td>${escapeHtml(it.name)}</td>
      <td>${it.qty}</td>
      <td>${escapeHtml(it.category || '')}</td>
      <td class="actions">
        <button class="action-btn" onclick="startEdit('${it.id}')">Edit</button>
        <button class="action-btn delete" onclick="removeItem('${it.id}')">Delete</button>
      </td>`
        body.appendChild(tr)
    })
}

function escapeHtml(s) { return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": "&#39;" })[c]) }

function addItem(e) {
    e.preventDefault()
    const name = $('name').value.trim()
    const qty = Math.max(1, parseInt($('qty').value) || 1)
    const category = $('category').value.trim()
    if (!name) return alert('Enter an item name')
    items.push({ id: Date.now().toString(36), name, qty, category })
    save(); render($('search').value); $('addForm').reset()
}

function startEdit(id) {
    const it = items.find(x => x.id === id); if (!it) return
    editingId = id
    $('editName').value = it.name
    $('editQty').value = it.qty
    $('editCategory').value = it.category
    const modal = $('editModal')
    modal.classList.remove('hidden')
    modal.style.display = 'flex'
}

function cancelEdit() {
    editingId = null;
    const modal = $('editModal')
    if (modal) { modal.classList.add('hidden'); modal.style.display = 'none' }
}

function saveEdit(e) {
    e.preventDefault();
    if (!editingId) return cancelEdit()
    try {
        const it = items.find(x => x.id === editingId);
        if (!it) throw new Error('editing item not found')
        it.name = $('editName').value.trim()
        it.qty = Math.max(1, parseInt($('editQty').value) || 1)
        it.category = $('editCategory').value.trim()
        save();
        render($('search').value)
    } catch (err) {
        console.error('Failed to save edit:', err)
    } finally {
        cancelEdit()
    }
}

function removeItem(id) {
    if (!confirm('Delete this item?')) return
    items = items.filter(x => x.id !== id)
    save(); render($('search').value)
}

function clearAll() { if (!confirm('Clear all items?')) return; items = []; save(); render() }

function init() {
    load();
    render();
    $('addForm').addEventListener('submit', addItem)
    $('editForm').addEventListener('submit', saveEdit)
    $('cancelEdit').addEventListener('click', cancelEdit)
    $('clearAll').addEventListener('click', clearAll)
    $('search').addEventListener('input', e => render(e.target.value))
}

window.startEdit = startEdit
window.removeItem = removeItem
document.addEventListener('DOMContentLoaded', init)
