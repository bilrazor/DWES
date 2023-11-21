package com.example.myothercatalog;


import org.json.JSONException;
import org.json.JSONObject;

public class PokemonData {
    private String name;
    private String imageUrl;

    private String description;

    // Constructor para datos estáticos
    public PokemonData(String name, String imageUrl , String description) {
        this.name = name;
        this.imageUrl = imageUrl;
        this.description = description;
    }

    // Constructor para procesar un objeto JSONObject
    public PokemonData(JSONObject robot) {
        try {
            // Suponiendo que el objeto JSON tiene las claves "name" y "imageUrl"
            this.name = robot.getString("name");
            this.imageUrl = robot.getString("image_url");
            this.description = robot.getString("description");
        } catch (JSONException e) {
            // Manejo de excepción en caso de un error en el procesamiento del JSON
            e.printStackTrace();
            // Puedes asignar valores predeterminados o manejar el error como consideres adecuado
            this.name = "Unknown";
            this.imageUrl = null;
        }
    }

    // Getters y setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
