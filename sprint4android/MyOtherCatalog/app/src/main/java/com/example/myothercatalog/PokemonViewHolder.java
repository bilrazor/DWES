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

    private final TextView textView;
    private final ImageView imageView;

    public PokemonViewHolder(@NonNull View itemView) {
        super(itemView);
        textView = itemView.findViewById(R.id.pokemon_name_text_view);
        imageView = itemView.findViewById(R.id.pokemon_image_view);
    }

    public void showData(PokemonData data, Activity activity) {
        textView.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                .into(imageView);

        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(activity, DetailActivity.class);
                intent.putExtra("name", data.getName());
                intent.putExtra("imageUrl", data.getImageUrl());
                // Si tienes una descripción, también puedes pasarla aquí
                intent.putExtra("description", data.getDescription());
                activity.startActivity(intent);
            }
        });
    }
    public void setOnClickListener(View.OnClickListener listener) {
        itemView.setOnClickListener(listener);
    }
}

