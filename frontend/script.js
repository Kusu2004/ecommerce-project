let events = [];


function addEvent(eventType) {

    const event = {
        event_type: eventType,
        timestamp: new Date().toISOString()
    };

    events.push(event);

    displayEvents();
}


function displayEvents() {

    const eventList = document.getElementById("eventList");

    if (events.length === 0) {

        eventList.innerHTML = "No events added yet";

        return;
    }

    eventList.innerHTML = "";

    events.forEach((event, index) => {

        const div = document.createElement("div");

        div.className = "event-item";

        div.innerHTML = `
            ${index + 1}. ${event.event_type}
        `;

        eventList.appendChild(div);
    });
}


function clearEvents() {

    events = [];

    displayEvents();

    document.getElementById("result").innerHTML = `
        <p class="empty">
            Add events and click "Classify Shopper"
        </p>
    `;
}


async function classifyUser() {

    const userId = document.getElementById("userId").value;

    if (events.length === 0) {

        alert("Please add at least one event");

        return;
    }

    const requestData = {

        user_id: userId,

        events: events

    };


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/classify",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(requestData)

            }
        );


        const data = await response.json();

        displayResult(data);


    } catch (error) {

        document.getElementById("result").innerHTML = `
            <p>
                Backend connection failed.
                Please check if FastAPI server is running.
            </p>
        `;

        console.error(error);

    }

}


function displayResult(data) {

    const classification = data.classification;

    const resultDiv = document.getElementById("result");


    const scoreHTML = Object.entries(
        classification.all_scores
    )
    .map(([state, score]) => {

        return `
            <li>
                <strong>${state}</strong>: ${score}%
            </li>
        `;

    })
    .join("");


    resultDiv.innerHTML = `

        <div class="result-box">


            <div class="state">

                ${classification.state}

            </div>


            <div class="confidence">

                Confidence:
                ${classification.confidence}

            </div>


            <div class="confidence-bar">

                <div
                    class="confidence-fill"
                    style="width: ${classification.score}%"
                    aria-label="Confidence ${classification.score}%"
                >

                    ${classification.score}%

                </div>

            </div>


            <div class="result-section">

                <strong>Evidence:</strong>

                <p>

                    ${classification.evidence.join("<br>")}

                </p>

            </div>


            <div class="result-section">

                <strong>Recommended Action:</strong>

                <p>

                    ${classification.recommended_action}

                </p>

            </div>


            <div class="result-section">

                <strong>Personalized Nudge:</strong>

                <p>

                    ${classification.nudge}

                </p>

            </div>


            <div class="result-section">

                <strong>All Shopper Scores:</strong>

                <ul>

                    ${scoreHTML}

                </ul>

            </div>


        </div>

    `;

}