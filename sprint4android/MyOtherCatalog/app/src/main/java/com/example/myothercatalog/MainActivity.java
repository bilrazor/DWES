package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private Context context = this; // Contexto de la actividad

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main); // Establece el layout para la actividad

        // Inicialización del RecyclerView en la interfaz de usuario
        RecyclerView recyclerView = findViewById(R.id.recycler_view);

        // Lista para almacenar los datos de los Pokémon
        List<PokemonData> allTheRobots = new ArrayList<>();

        // Solicitud de red para obtener datos de Pokémon
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/CarlosAfundacion/catalog/main/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        // Procesa cada objeto JSON y lo añade a la lista
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                JSONObject robot = response.getJSONObject(i);
                                PokemonData data = new PokemonData(robot);
                                allTheRobots.add(data);
                            } catch (JSONException e) {
                                throw new RuntimeException(e);
                            }
                        }
                        // Configura el adaptador del RecyclerView y el LayoutManager
                        PokemonRecyclerViewAdapter adapter = new PokemonRecyclerViewAdapter(allTheRobots, MainActivity.this);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(MainActivity.this));
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Maneja errores de la solicitud de red
                    }
                }
        );

        // Añade la solicitud a la cola de solicitudes de Volley
        RequestQueue queue = Volley.newRequestQueue(this);
        queue.add(request);
    }
}