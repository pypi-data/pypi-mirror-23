var apiUrl = "/digger/";
var tasksUrl = "tasks/";

new Vue({
  el: "#app",
  data: {
    baseUrl: "https://app.activecollab.com/148987",
    completedTasksCount: 0,
    isReady: false,
    leader_id: null,
    newTask: { name: "", description: "" },
    notification: null,
    project: null,
    task_lists: null,
    tasks: null
  },
  created: function() {
    this.getTasks();
  },
  filters: {
    formatDate: function(v) {
      var d = new Date(v * 1000);
      return d.toDateString();
    }
  },
  methods: {
    getTasks: function() {
      var self = this;

      var xhr = new XMLHttpRequest();
      xhr.open("GET", apiUrl + tasksUrl);

      xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);

        if (response.project) {
          self.completedTasksCount = response.completed_tasks_count;
          self.leader_id = response.project.leader_id;
          self.project = response.project;
          self.task_lists = response.task_lists;
          self.tasks = response.tasks;
        } else {
          self.notification = {
            status: 1,
            message: "Error getting project information.<br>" +
              response.error +
              ": " +
              response.message
          };
        }

        self.isReady = true;
      };

      xhr.send();
    },
    addTask: function() {
      var name = this.newTask.name;
      var body = this.newTask.description;

      if (!name) {
        return;
      }

      var self = this;

      var xhr = new XMLHttpRequest();
      xhr.open("POST", apiUrl + tasksUrl);

      xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xhr.setRequestHeader("X-CSRFToken", Cookie.get("csrftoken"));

      xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
          var response = JSON.parse(xhr.responseText);
          if (response.single) {
            self.tasks.push(response.single);
            self.notification = {
              status: 0,
              message: 'Task "' + name + '" created successfully.'
            };
          } else {
            self.notification = {
              status: 1,
              message: 'Error creating task "' +
                name +
                '".<br>' +
                response.error +
                ": " +
                response.message
            };
          }
        } else if (xhr.readyState == XMLHttpRequest.DONE && xhr.status != 200) {
          self.notification = {
            status: 1,
            message: 'Error creating task "' +
              name +
              '".<br>' +
              response.error +
              ": " +
              response.message
          };
        }
      };

      xhr.send("name=" + name + "&body=" + body);

      this.newTask.name = "";
      this.newTask.description = "";
    },
    clearTask: function() {
      this.newTask.name = "";
      this.newTask.description = "";
    },
    removeNotification: function() {
      this.notification = null;
    }
  }
});

