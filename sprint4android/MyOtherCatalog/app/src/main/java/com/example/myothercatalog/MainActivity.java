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
    private Context context = this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        Activity activity = this;

        List<PokemonData> allTheRobots = new ArrayList<>();
       /* data.add(new PokemonData("Bukbasaur" ,"https://raw.githubusercontent.com/bilrazor/DWES/main/resources/imagen1Edited.png"));
        data.add(new PokemonData("Bukbasaur" ,"https://raw.githubusercontent.com/bilrazor/DWES/main/resources/imagen1Edited.png"));
        data.add(new PokemonData("Bukbasaur" ,"https://raw.githubusercontent.com/bilrazor/DWES/main/resources/imagen1Edited.png"));
        data.add(new PokemonData("Bukbasaur" ,"https://raw.githubusercontent.com/bilrazor/DWES/main/resources/imagen1Edited.png"));
        data.add(new PokemonData("Bukbasaur" ,"https://raw.githubusercontent.com/bilrazor/DWES/main/resources/imagen1Edited.png"));
        data.add(new PokemonData("Bukbasaur" ,"https://raw.githubusercontent.com/bilrazor/DWES/main/resources/imagen1Edited.png"));
        data.add(new PokemonData("Bukbasaur" ,"https://raw.githubusercontent.com/bilrazor/DWES/main/resources/imagen1Edited.png"));
        PokemonRecyclerViewAdapter adapter = new PokemonRecyclerViewAdapter(data , this);
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
    }*/
       /* Button buttonMain = findViewById(R.id.button_main);
        buttonMain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(context, DetailActivity.class);
                context.startActivity(intent);
            }
        });*/
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/CarlosAfundacion/catalog/main/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                JSONObject robot = response.getJSONObject(i);
                                PokemonData data = new PokemonData(robot);
                                allTheRobots.add(data);
                            } catch (JSONException e) {
                                throw new RuntimeException(e);
                            }
                        }
                        PokemonRecyclerViewAdapter adapter = new PokemonRecyclerViewAdapter(allTheRobots, activity);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));

                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                    }

                }

        );
        RequestQueue cola = Volley.newRequestQueue(this);
        cola.add(request);
    }
}