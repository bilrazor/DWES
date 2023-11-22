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
    // Datos y actividad asociada al adaptador
    private List<PokemonData> allTheData;
    private Activity activity;

    // Constructor del adaptador
    public PokemonRecyclerViewAdapter(List<PokemonData> dataSet, Activity activity) {
        this.allTheData = dataSet;
        this.activity = activity;
    }

    @NonNull
    @Override
    public PokemonViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Infla el layout para cada elemento de la lista
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.pokemon_view_holder, parent, false);
        return new PokemonViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull PokemonViewHolder holder, int position) {
        // Asigna los datos al ViewHolder
        PokemonData dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }

    @Override
    public int getItemCount() {
        // Retorna el tamaño de la lista de datos
        return allTheData.size();
    }
}
