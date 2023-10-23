document.addEventListener('DOMContentLoaded', function() {
    // Extract tournament name from the URL
    const tournamentNameWithUnderscores = window.location.pathname.split('/').pop().replace(/-/g, '_');
    const tournamentNameWithHyphens = window.location.pathname.split('/').pop();

    // Construct API endpoint URLs for both formats
    const apiUrlWithUnderscores = `https://ali-daixin-tian.net/api/get_teams?tournament_slug=${tournamentNameWithUnderscores}`;
    const apiUrlWithHyphens = `https://ali-daixin-tian.net/api/get_teams?tournament_slug=${tournamentNameWithHyphens}`;

    // Make API requests
    Promise.all([
        fetch(apiUrlWithUnderscores).then(response => response.json()),
        fetch(apiUrlWithHyphens).then(response => response.json())
    ])
    .then(([teamsWithUnderscores, teamsWithHyphens]) => {
        // Use the response with more items
        const teamsToUse = teamsWithUnderscores.length >= teamsWithHyphens.length ? teamsWithUnderscores : teamsWithHyphens;

        // Handle the response here (teams data)
        const teamCapitalLetters = teamsToUse.map(team => {
            // Get the first character of the team name in lowercase
            const firstChar = team.trim().charAt(0).toLowerCase();
            // If the first character is a number, set it to 'number'
            return isNaN(firstChar) ? firstChar : 'number';
        }).join('%7C');

        // Sanitize team names (replace spaces with dashes and convert to lowercase)
        const sanitizedTeamNames = teamsToUse.map(team => team.trim().replace(/\s+/g, '-').toLowerCase()).join('%7C');

        // Construct the redirect URL with team-capital-letter and sanitized team names
        const redirectUrl = `https://riftranks.webflow.io/team-rankings?team-capital-letter=${teamCapitalLetters}&team-names-for-reference=${sanitizedTeamNames}`;

        // Redirect to the generated URL
        window.location.href = redirectUrl;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
