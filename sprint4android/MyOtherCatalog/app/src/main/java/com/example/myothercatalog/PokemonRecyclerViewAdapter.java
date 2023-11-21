package com.example.myothercatalog;

import android.app.Activity;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class PokemonRecyclerViewAdapter extends RecyclerView.Adapter<PokemonViewHolder> {

    private List<PokemonData> allTheData;
    private Activity activity;

    public PokemonRecyclerViewAdapter(List<PokemonData> dataSet, Activity activity) {
        this.allTheData = dataSet;
        this.activity = activity;
    }

    @NonNull
    @Override
    public PokemonViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.pokemon_view_holder, parent , false );
        return new PokemonViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull PokemonViewHolder holder, int position) {
        PokemonData dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered , activity);
        holder.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(activity, DetailActivity.class);
                // Aquí puedes añadir extras al intent si necesitas pasar datos a DetailActivity
                activity.startActivity(intent);
            }
        });
    }

    @Override
    public int getItemCount() {
        return allTheData.size();
    }
}
