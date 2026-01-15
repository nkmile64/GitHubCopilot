// Task Manager Application
class TaskManager {
    constructor() {
        this.tasks = [];
        this.currentFilter = 'all';
        this.taskId = 0;
        this.init();
    }

    init() {
        this.loadTasks();
        this.setupEventListeners();
        this.render();
    }

    setupEventListeners() {
        // Form submission
        const taskForm = document.getElementById('taskForm');
        taskForm.addEventListener('submit', (e) => this.handleAddTask(e));

        // Clear completed button
        const clearButton = document.getElementById('clearCompleted');
        clearButton.addEventListener('click', () => this.clearCompletedTasks());

        // Filter buttons
        const filterButtons = document.querySelectorAll('.filter-button');
        filterButtons.forEach(button => {
            button.addEventListener('click', (e) => this.setFilter(e.target.dataset.filter));
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                taskForm.dispatchEvent(new Event('submit'));
            }
        });

        // Dark mode toggle
        const darkModeToggle = document.getElementById('darkModeToggle');
        darkModeToggle.addEventListener('click', () => this.toggleDarkMode());

        // Load dark mode preference
        this.initDarkMode();
    }

    handleAddTask(e) {
        e.preventDefault();

        const input = document.getElementById('taskInput');
        const errorDiv = document.getElementById('taskError');
        const text = input.value.trim(); // Trim whitespace

        // Validation
        if (!text) {
            this.showError(errorDiv, 'Please enter a task');
            return;
        }

        if (text.length > 500) {
            this.showError(errorDiv, 'Task must be less than 500 characters');
            return;
        }

        // Clear error
        errorDiv.classList.remove('show');

        // Add task
        this.addTask(text);
        input.value = '';
        input.focus();
    }

    showError(element, message) {
        element.textContent = message;
        element.classList.add('show');
        setTimeout(() => {
            element.classList.remove('show');
        }, 3000);
    }

    addTask(text) {
        const task = {
            id: this.taskId++,
            text: text,
            completed: false,
            createdAt: new Date().toISOString()
        };

        this.tasks.unshift(task);
        this.saveTasks();
        this.render();
    }

    deleteTask(id) {
        this.tasks = this.tasks.filter(task => task.id !== id);
        this.saveTasks();
        this.render();
    }

    toggleTask(id) {
        const task = this.tasks.find(task => task.id === id);
        if (task) {
            task.completed = !task.completed;
            this.saveTasks();
            this.render();
        }
    }

    clearCompletedTasks() {
        const completedCount = this.tasks.filter(t => t.completed).length;

        if (completedCount === 0) return;

        if (confirm(`Delete ${completedCount} completed task${completedCount > 1 ? 's' : ''}?`)) {
            this.tasks = this.tasks.filter(task => !task.completed);
            this.saveTasks();
            this.render();
        }
    }

    setFilter(filter) {
        this.currentFilter = filter;

        // Update button states
        document.querySelectorAll('.filter-button').forEach(btn => {
            const isActive = btn.dataset.filter === filter;
            btn.classList.toggle('active', isActive);
            btn.setAttribute('aria-pressed', isActive);
        });

        this.render();
    }

    getFilteredTasks() {
        switch (this.currentFilter) {
            case 'active':
                return this.tasks.filter(task => !task.completed);
            case 'completed':
                return this.tasks.filter(task => task.completed);
            default:
                return this.tasks;
        }
    }

    saveTasks() {
        try {
            localStorage.setItem('tasks', JSON.stringify(this.tasks));
            localStorage.setItem('taskId', String(this.taskId));
        } catch (e) {
            console.error('Failed to save tasks:', e);
        }
    }

    loadTasks() {
        try {
            const saved = localStorage.getItem('tasks');
            const savedId = localStorage.getItem('taskId');

            if (saved) {
                this.tasks = JSON.parse(saved);
            }

            if (savedId) {
                this.taskId = parseInt(savedId, 10);
            }
        } catch (e) {
            console.error('Failed to load tasks:', e);
            this.tasks = [];
        }
    }

    updateStats() {
        const activeCount = this.tasks.filter(t => !t.completed).length;
        const completedCount = this.tasks.filter(t => t.completed).length;

        document.getElementById('activeCount').textContent = activeCount;
        document.getElementById('completedCount').textContent = completedCount;

        // Disable clear button if no completed tasks
        const clearButton = document.getElementById('clearCompleted');
        clearButton.disabled = completedCount === 0;
    }

    render() {
        this.updateStats();
        this.renderTasks();
    }

    renderTasks() {
        const container = document.getElementById('tasksContainer');
        const filteredTasks = this.getFilteredTasks();

        if (filteredTasks.length === 0) {
            container.innerHTML = `
                <div class="empty-state">
                    <p>${this.getEmptyStateMessage()}</p>
                </div>
            `;
            return;
        }

        const template = document.getElementById('taskTemplate');
        container.innerHTML = '';

        filteredTasks.forEach(task => {
            const clone = template.content.cloneNode(true);

            // Set task data
            const article = clone.querySelector('article');
            article.dataset.taskId = task.id;

            if (task.completed) {
                article.classList.add('completed');
            }

            // Checkbox
            const checkbox = clone.querySelector('.task-checkbox-input');
            checkbox.checked = task.completed;
            checkbox.addEventListener('change', () => this.toggleTask(task.id));
            checkbox.setAttribute('aria-label', `Mark "${task.text}" as ${task.completed ? 'incomplete' : 'complete'}`);

            // Task text
            const textElement = clone.querySelector('.task-text');
            textElement.textContent = task.text;

            // Delete button
            const deleteBtn = clone.querySelector('.delete-button');
            deleteBtn.addEventListener('click', () => this.deleteTask(task.id));
            deleteBtn.setAttribute('aria-label', `Delete "${task.text}"`);

            container.appendChild(clone);
        });
    }

    getEmptyStateMessage() {
        switch (this.currentFilter) {
            case 'active':
                return 'No active tasks. Great job!';
            case 'completed':
                return 'No completed tasks yet.';
            default:
                return 'No tasks yet. Add one to get started!';
        }
    }

    toggleDarkMode() {
        const isDarkMode = document.documentElement.classList.contains('dark-mode');
        this.setDarkMode(!isDarkMode);
    }

    setDarkMode(enable) {
        const toggle = document.getElementById('darkModeToggle');
        const icon = toggle.querySelector('.toggle-icon');

        if (enable) {
            document.documentElement.classList.add('dark-mode');
            icon.textContent = '☀️';
            toggle.setAttribute('aria-pressed', 'true');
            toggle.setAttribute('title', 'Toggle light mode');
            localStorage.setItem('darkMode', 'true');
        } else {
            document.documentElement.classList.remove('dark-mode');
            icon.textContent = '🌙';
            toggle.setAttribute('aria-pressed', 'false');
            toggle.setAttribute('title', 'Toggle dark mode');
            localStorage.setItem('darkMode', 'false');
        }
    }

    initDarkMode() {
        const savedDarkMode = localStorage.getItem('darkMode') === 'true';
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const isDarkMode = savedDarkMode || (localStorage.getItem('darkMode') === null && prefersDark);

        if (isDarkMode) {
            this.setDarkMode(true);
        }
    }
}

// Initialize the app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new TaskManager();
});
