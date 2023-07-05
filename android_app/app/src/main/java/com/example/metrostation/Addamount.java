package com.example.metrostation;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONObject;

public class Addamount extends AppCompatActivity  implements JsonResponse {
    EditText e1;
    String amount;
    Button b1;
    ListView l1;
    String[] amounts, statu, date, value, request_id;
    SharedPreferences sh;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_addamount);


        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        e1 = (EditText) findViewById(R.id.etcomplaint);
        b1 = (Button) findViewById(R.id.button);
        l1 = (ListView) findViewById(R.id.lvview);

//        l1.setOnItemClickListener(this);


        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                amount = e1.getText().toString();


                JsonReq JR = new JsonReq();
                JR.json_response = (JsonResponse) Addamount.this;
                String q = "/Addamount?amount=" + amount + "&log=" + login.logid + "&logid=" + sh.getString("logid", "");
                q = q.replace(" ", "%20");
                JR.execute(q);

            }
        });
    }

    @Override
    public void response(JSONObject jo) {
        try {


            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                Toast.makeText(getApplicationContext(), " SUCCESSFULLY", Toast.LENGTH_LONG).show();
                startActivity(new Intent(getApplicationContext(), Userhome.class));

            } else {

                Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
            }



        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }
    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);
    }
    }
