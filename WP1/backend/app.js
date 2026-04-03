const API = "http://127.0.0.1:5000";

if (!name || !coef) {
    alert("Remplis tous les champs");
    return;
}

if (grade < 0 || grade > 20) {
    alert("La note doit être entre 0 et 20");
    return;
}

// Ajouter matière
async function addSubject() {
    const name = document.getElementById("name").value;
    const coef = document.getElementById("coef").value;

    await fetch(`${API}/subjects`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ name, coef })
    });

    document.getElementById("result").innerText = "Matière ajoutée !";
}

// Ajouter note
async function addGrade() {
    const subject_id = document.getElementById("subject_id").value;
    const grade = document.getElementById("grade").value;

    await fetch(`${API}/grades`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ subject_id, grade })
    });

   document.getElementById("result").innerText = "Note ajoutée !";

}

// Moyenne
async function getAverage() {
    const res = await fetch(`${API}/average`);
    const data = await res.json();

    document.getElementById("result").innerText =
        "Moyenne : " + data.average;
}

try {
    const res = await fetch(...$);
} catch (error) {
    document.getElementById("result").innerText = "Erreur serveur";
}