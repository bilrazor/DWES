package com.example.myothercatalog;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.google.android.material.button.MaterialButton;

import de.hdodenhof.circleimageview.CircleImageView;

public class DetailActivity extends AppCompatActivity {
    //Este es el método principal donde se inicializa la actividad.
    // Se llama cuando se crea la actividad por primera vez.
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //Establece el diseño (layout) de la actividad usando el archivo XML
        setContentView(R.layout.detail_activity);
        // findViewById Se usa para encontrar y asignar vistas del archivo XML
        // a variables en el código. Aquí se obtienen referencias
        // a TextView para el título y la descripción, y a CircleImageView para la imagen.
        TextView titleTextView = findViewById(R.id.firstText);
        CircleImageView imageView = findViewById(R.id.imageView);
        TextView descriptionTextView = findViewById(R.id.descriptionText);
        //getIntent().getExtras(): Obtiene cualquier dato adicional que se haya pasado a esta actividad.
        Bundle extras = getIntent().getExtras();
        if (extras != null) {

            String name = extras.getString("name");
            String imageUrl = extras.getString("imageUrl");
            String description = extras.getString("description");
            //Se establecen los textos de los TextView con los
            // datos recibidos (name y description).
            titleTextView.setText(name);
            descriptionTextView.setText(description);
            //Se carga una imagen desde una URL
            Glide.with(this)
                    .load(imageUrl)
                    .into(imageView);
        }
        // Obtener referencia del botón
        MaterialButton likeButton = findViewById(R.id.buttonLike);

        // Establecer escuchador de clics para el botón
        likeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Mostrar un Toast cuando se haga clic
                Toast.makeText(DetailActivity.this, "like +1", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
