document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.container-default.w-container');

    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('query') + ', include the team name if possible';

    // API endpoint and credentials (similar to previous code)
    const apiUrl = 'https://eu-central-1.data.tidbcloud.com/api/v1beta/app/chat2query-YdBxnPzY/endpoint/chat2data';
    const publicKey = 'q472yi96';
    const privateKey = '6bc870a3-43f7-4dbb-a7f8-b97eaf50a565';
    const credentials = `${publicKey}:${privateKey}`;
    const encodedCredentials = btoa(credentials);

    const data = {
        cluster_id: '1379661944646225457',
        database: 'test',
        tables: ['Riot_AWS_team_ranking'],
        instruction: query,
    };

    // Make API call
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Basic ${encodedCredentials}`
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(apiResponse => {
        const columns = apiResponse.data.columns.map(column => column.col);
        const rows = apiResponse.data.rows;

        // Render cards based on API response
        const responseContainer = document.createElement('div');
        responseContainer.classList.add('response-container');

        rows.forEach(row => {
            const responseCard = document.createElement('div');
            responseCard.classList.add('response-card');

            responseCard.addEventListener('click', function() {
                const teamName = row['team_name'].replace(/'/g, '').toLowerCase().replace(/ /g, '-'); 
                const link_to_detail_page = `https://riftranks.webflow.io/teams/${teamName}`;
                window.location.href = link_to_detail_page;
            });

            columns.forEach(column => {
                const attributeCard = document.createElement('div');
                attributeCard.classList.add('attribute-card');
                attributeCard.innerText = column;

                const valueCard = document.createElement('div');
                valueCard.classList.add('value-card');
                valueCard.innerText = row[column] || 'N/A';

                // Append attribute and value cards to the response card
                responseCard.appendChild(attributeCard);
                responseCard.appendChild(valueCard);
            });

            // Append the response card to the response container
            responseContainer.appendChild(responseCard);
        });

        // document.body.appendChild(responseContainer);
        container.appendChild(responseContainer);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});