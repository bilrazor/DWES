package com.example.myothercatalog;

import android.os.Bundle;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

import de.hdodenhof.circleimageview.CircleImageView;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);

        TextView titleTextView = findViewById(R.id.firstText);
        CircleImageView imageView = findViewById(R.id.imageView);
        TextView descriptionTextView = findViewById(R.id.descriptionText);

        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            String name = extras.getString("name");
            String imageUrl = extras.getString("imageUrl");
            String description = extras.getString("description");

            titleTextView.setText(name);
            descriptionTextView.setText(description); // Descomenta esta línea si pasas la descripción

            Glide.with(this)
                    .load(imageUrl)
                    .into(imageView);
        }
    }
}

