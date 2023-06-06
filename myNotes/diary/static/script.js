notes = document.querySelectorAll(".notes-feed .note")
noteView = document.querySelector(".notes-preview .note")
search = document.querySelector("header input")
var current_note = notes[0]

function clearPreview(){
    result = confirm("Вы точно хотите отчистить заметку?")
    if (result){
        noteView.querySelector(".note-text textarea").value = ""
        noteView.querySelector(".note-header input").value = ""
        noteView.setAttribute("noteid", "")
        noteView.querySelector('button[name="btn_save_note"').disabled=true
        noteView.querySelector('button[name="btn_delete_note"').disabled=true
    }
}

function updateNoteView(note){
    current_note = note
    noteView.querySelector(".note-text textarea").value = note.querySelector(".note-text").innerText
    noteView.querySelector(".note-header input").value = note.querySelector(".note-header").innerText
    noteView.querySelector("#noteId input").value = note.getAttribute("noteid")
    noteView.setAttribute("noteid", note.getAttribute("noteid"))
    noteView.querySelector('button[name="btn_save_note"').disabled=false
    noteView.querySelector('button[name="btn_delete_note"').disabled=false
    console.log("gee")
}

function searchForNote(){
    search_request = search.value
    for (element of notes){
        console.log(element)
        if (search_request == ""){
            element.setAttribute("style", "display: block")
        }else if (element.querySelector(".note-header").innerText.toLowerCase().includes(search_request.toLowerCase(), 0)){
            element.setAttribute("style", "display: block")
        }else{
            element.setAttribute("style", "display: none")
        }
    }
}

function updateNotePreview(){
    console.log("updated")
    current_note.querySelector(".note-text").innerText = noteView.querySelector("textarea").value
    current_note.querySelector(".note-header").innerText = noteView.querySelector("input").value
}

noteView.querySelector("textarea").addEventListener("change", updateNotePreview)
search.addEventListener("change", searchForNote);