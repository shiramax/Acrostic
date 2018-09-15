function addComment() {
    var linebreak = document.createElement("br");
    var container = document.getElementById("container");
    var line = document.createElement("INPUT");
    line.setAttribute("type", "text");
    line.style.width="80%";
    var submit = document.createElement("INPUT");
    submit.setAttribute("type", "submit");
    submit.name = "Add";
    container.appendChild(linebreak);
    container.appendChild(line);
    container.appendChild(submit);
}