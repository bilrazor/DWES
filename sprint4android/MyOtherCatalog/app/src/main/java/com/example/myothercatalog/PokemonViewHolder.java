package com.example.myothercatalog;

import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class PokemonViewHolder extends RecyclerView.ViewHolder {
    // Referencias a las vistas en el layout
    private final TextView textView;
    private final ImageView imageView;

    public PokemonViewHolder(@NonNull View itemView) {
        super(itemView);
        textView = itemView.findViewById(R.id.pokemon_name_text_view);
        imageView = itemView.findViewById(R.id.pokemon_image_view);
    }

    public void showData(PokemonData data, Activity activity) {
        // Configura los datos en las vistas
        textView.setText(data.getName());
        Glide.with(itemView.getContext()).load(data.getImageUrl()).into(imageView);

        // Establece un clic listener para el elemento
        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Inicia DetailActivity y pasa datos adicionales
                Intent intent = new Intent(activity, DetailActivity.class);
                intent.putExtra("name", data.getName());
                intent.putExtra("imageUrl", data.getImageUrl());
                intent.putExtra("description", data.getDescription()); // Pasa la descripción si está disponible
                activity.startActivity(intent);
            }
        });
    }

    public void setOnClickListener(View.OnClickListener listener) {
        // Método para establecer un listener personalizado si es necesario
        itemView.setOnClickListener(listener);
    }
}

