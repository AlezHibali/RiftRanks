## RiftRanks: League of Legends Team Rankings

Welcome to RiftRanks, your go-to platform for discovering the latest and most accurate rankings of professional League of Legends teams. This project is dedicated to providing gamers and esports enthusiasts with up-to-date and reliable information about their favorite teams, backed by advanced technology and seamless integration of various services.

### Overview

RiftRanks utilizes a robust tech stack to deliver its services:

- **Amazon Web Services (AWS):** We leverage AWS services including EC2, Route53, and S3 to power our platform. EC2 ensures our Flask APIs run 24/7, guaranteeing real-time data. Route53 handles domain registration and links to EC2's IPv4 address, enabling secure HTTPS connections for our APIs. S3 stores our datasets, and in conjunction with TiDB, facilitates our 'Prompt2Data' search feature.

- **Principal Component Analysis (PCA):** Our ranking system is based on PCA, allowing us to process vast amounts of data from the past three years of League of Legends matches, providing accurate and insightful team rankings.

### Dependencies

- Flask
- BeautifulSoup
- Requests
- TiDB
- AWS SDKs (EC2, Route53, S3)

### Installation

No need to install, everything is deployed properly and can access the webpage directly [https://riftranks.webflow.io](https://riftranks.webflow.io/).

### Usage

Before visiting our website, it's crucial to run the API backend:

```bash
python app.py
```

This command will launch the backend, ensuring real-time data availability.

Visit [https://riftranks.webflow.io](https://riftranks.webflow.io/) to experience our cutting-edge team rankings. Please note, for specific features such as favoriting teams or accessing personalized data, you may need to create an account.

### Support and Feedback

For any questions, issues, or feedback, don't hesitate to reach out to us via GitHub or email us at support@riftranks.com.

### Acknowledgements

We extend our gratitude to Amazon Web Services for empowering our platform and the League of Legends community. Your support has made RiftRanks possible.

---

Got questions, suggestions, or just want to chat about all things gaming? We're all ears! Reach out to us at [ali.daixin.tian@gmail.com](ali.daixin.tian@gmail.com).
