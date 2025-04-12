<h1> BOTANICA API. 🌸 </h1>

<div align='center'>
<img src="assets/images/api-botanica.jpeg">
</div>
<p align="left"> <small> 𝓐𝓻𝓽 𝓫𝔂: <a href="https://www.instagram.com/lotusteapot?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="> @lotusteapot </a> </small> </p>

The goal of the API is to create and manage some plants. All this in a very simplified context. Using only the basic functionalities for demonstration.


> Why are flowers separated from plants? Because every flower is a plant, but not every plant is a flower! And I hope to divide it into more categories later.

The implementation is based on 3 pillars:

# A API. 🍃

The API is divided into three routers 🪢:

- `Accounts`: Account and API access management.

- `Plants`: Plant management.

- `Flowers`: Plant management.



```mermaid
graph TD
    A[Botany API] --> B[Access Control / Account Management]
    A --> C[Plant Management]
    A --> D[Flower Management]

    B --> E[Account Management]
    B --> F[JWT Access]

    E --> G[Create]
    E --> H[Update]
    E --> I[Delete]

    C --> J[CRUD]
    D --> K[CRUD]
```

WARNING ⚠️
> Please note: This project is a demonstration only and is not a hosted API.