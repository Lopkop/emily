const form = document.getElementById("todo-id");
const input = document.getElementById("d");
const todoLane = document.getElementById("todo-lane");

form.addEventListener("submit", (e) => {
  const value = input.value;

  if (!value) return;

  const newTask = document.createElement("textarea");
  newTask.classList.add("task");
  newTask.setAttribute("draggable", "true");
  newTask.innerText = value;

  newTask.addEventListener("dragstart", () => {
    newTask.classList.add("is-dragging");
  });

  newTask.addEventListener("dragend", () => {
    newTask.classList.remove("is-dragging");
  });

  todoLane.appendChild(newTask);

  input.value = "";
});
