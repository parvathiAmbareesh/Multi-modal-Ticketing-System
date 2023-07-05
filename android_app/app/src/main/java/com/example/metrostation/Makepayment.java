package com.example.metrostation;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONObject;

public class Makepayment extends AppCompatActivity implements JsonResponse {
    EditText e1,e2,e3,e4,e5;
    Button b1;
    String card,cvv,exp,name,amount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_makepayment);
        e1=(EditText)findViewById(R.id.etcard);
        e2=(EditText)findViewById(R.id.etcvv);
        e3=(EditText)findViewById(R.id.etexp);
        e4=(EditText)findViewById(R.id.etname);
        e5=(EditText)findViewById(R.id.etamount);

        e5.setEnabled(false);

        b1=(Button)findViewById(R.id.button);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                card=e1.getText().toString();
                cvv=e2.getText().toString();
                exp=e3.getText().toString();
                name=e4.getText().toString();
                amount=e5.getText().toString();
                if (e1.getText().toString().length() != 16) {
                    Toast.makeText(getApplicationContext(), "16 Digit",
                            Toast.LENGTH_LONG).show();
                    e1.setError("enter 16 digit");
                    e1.setFocusable(true);

                } else if (e2.getText().toString().length() != 3) {
                    Toast.makeText(getApplicationContext(), "3 Digit",
                            Toast.LENGTH_LONG).show();
                    e2.setError("enter 3 digit");
                    e2.setFocusable(true);

                }

                else {

                    JsonReq JR = new JsonReq();
                    JR.json_response = (JsonResponse) Makepayment.this;
                    String q = "/usermakepayment?amt="  +"&fromplace=" +exp +"&toplace="+name+"&rid=";
                    q = q.replace(" ", "%20");
                    JR.execute(q);
                }
            }
        });

    }

    @Override
    public void response(JSONObject jo) {
        try {


            String status = jo.getString("status");
            Log.d("pearl", status);


            if (status.equalsIgnoreCase("success")) {
                Toast.makeText(getApplicationContext(), "PAID SUCCESSFULLY", Toast.LENGTH_LONG).show();
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
