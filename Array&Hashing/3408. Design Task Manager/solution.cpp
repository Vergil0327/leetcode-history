using pii = pair<int,int>;

class TaskManager {
    set<vector<int>, greater<vector<int>>> s; // Descending order
    unordered_map<int, int> task2user;
    map<pii, int> user2priority;
    
public:
    TaskManager(vector<vector<int>>& tasks) {
        for (auto& task : tasks) {
            int userId = task[0], taskId = task[1], priority = task[2];
            this->add(userId, taskId, priority);
        }
    }
    
    void add(int userId, int taskId, int priority) {
        task2user[taskId] = userId;
        user2priority[{userId, taskId}] = priority;
        s.insert({priority, taskId, userId});
    }
    
    void edit(int taskId, int newPriority) {
        int userId = task2user[taskId];
        int old_priority = user2priority[{userId, taskId}];
        s.erase({old_priority, taskId, userId});
        s.insert({newPriority, taskId, userId});
        user2priority[{userId, taskId}] = newPriority;
    }
    
    void rmv(int taskId) {
        int userId = task2user[taskId];
        int priority = user2priority[{userId, taskId}];
        
        task2user.erase(taskId);
        user2priority.erase({userId, taskId});
        s.erase({priority, taskId, userId});
    }
    
    int execTop() {
        if (s.empty()) return -1;
        
        auto element = *s.begin(); // First element (highest priority)
        int taskId = element[1];
        this->rmv(taskId);

        int userId = element[2];
        return userId;
    }
};

// better performance
struct Task {
    int priority, taskId;
    bool operator<(const Task &other) const {
        if (priority == other.priority) return taskId < other.taskId;
        return priority < other.priority;
    }
};

class TaskManager {
    unordered_map<int, pair<int,int>> taskMap; // taskId -> (userId, priority)
    priority_queue<Task> pq;

public:
    TaskManager(vector<vector<int>>& tasks) {
        for (auto &t : tasks) {
            int u = t[0], id = t[1], p = t[2];
            this->add(u, id, p);
        }
    }

    void add(int userId, int taskId, int priority) {
        taskMap[taskId] = {userId, priority};
        pq.push({priority, taskId});
    }

    void edit(int taskId, int newPriority) {
        auto& info = taskMap[taskId];
        info.second = newPriority;
        pq.push({newPriority, taskId}); // lazy update
    }

    void rmv(int taskId) {
        taskMap.erase(taskId); // lazy delete
    }

    int execTop() {
        while (!pq.empty()) {
            auto top = pq.top(); pq.pop();
            int id = top.taskId;
            if (taskMap.count(id) && taskMap[id].second == top.priority) {
                int userId = taskMap[id].first;
                taskMap.erase(id);
                return userId;
            }
            // else: old/invalid entry, skip
        }
        return -1;
    }
};